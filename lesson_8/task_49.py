"""
Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
для изменения и удаления данных
"""
from os import system
from os import path

file_base = "base.txt"
last_id = 0
all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global last_id, all_data

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
    return []


def list_to_str(_list, sep):
    if _list:
        return sep.join(_list)
    else:
        return "No entries"


def str_to_list(_str):
    if _str:
        return _str.split()


def show_all():
    clear_terminal()
    print("All entries:")
    print(list_to_str(all_data, "\n"))
    input("Enter anything to continue...")


def add_record():
    clear_terminal()

    entry = input_entry_data("Add a record")
    entry_str = list_to_str(entry, " ")

    matches = match_entries(entry[0])
    if matches:
        message = "New entry:\n" \
                  + entry_str \
                  + "\nFound entry(ies) with the same phone number:\n" \
                  + list_to_str(matches, "\n") \
                  + "\nAdd the entry anyway? (Y/N): "
    else:
        message = "New entry\n" \
                  + entry_str \
                  + "\nAdd the entry? (Y/N): "

    if confirm(message):
        if append_str(str(last_id + 1) + " " + entry_str):
            print("Successfully added")
        else:
            print("Fail to add entry!")
        input("Enter anything to continue...")


def search_record():
    while True:
        clear_terminal()
        print("Search a record")

        input_str = input("Input string to search: ").strip()

        matches = match_entries(input_str)

        message = f"Entries with \"{input_str}\":\n" \
                  + list_to_str(matches, "\n") \
                  + "\nSearch another one? Y/N: "

        if not confirm(message):
            return


def change_record():
    while True:
        index = get_index("Change a record")

        if index < 0:
            return

        old_entry = all_data[index]

        new_data = new_entry_data(old_entry)

        if not new_data:
            return

        new_entry = old_entry.split()[0] + " " + list_to_str(new_data, " ")

        matches = match_entries(new_data[0])
        if len(matches) == 1:
            matches = []
        else:
            matches.remove(old_entry)

        if matches:
            message = "New entry data:\n" \
                      + new_entry \
                      + "\nFound entry(ies) with the same phone number:\n" \
                      + list_to_str(matches, "\n") \
                      + "\nChange the entry anyway? (Y/N): "
        else:
            message = "New entry data:\n" \
                      + new_entry \
                      + "\nChange the entry? (Y/N): "

        if confirm(message):
            all_data[index] = new_entry
            update_base()
            print("Successfully changed")
            input("Enter anything to continue...")

        return


def new_entry_data(old_entry):
    header = "Change the record:\n" \
             + old_entry \
             + "\nEnter new data (or input empty string to keep old one)"

    old_data = old_entry.split()[1:]

    while True:
        clear_terminal()
        new_data = input_entry_data(header)
        count = 0

        for idx, item in enumerate(new_data):
            if not item:
                new_data[idx] = old_data[idx]
                count += 1

        if count == len(old_entry):
            message = "Nothing changed. Try again? Y/N: "
            if not confirm(message):
                return []

        return new_data


def delete_record():
    index = get_index("Delete a record")

    if index < 0:
        return

    old_entry = all_data[index]

    if confirm(old_entry + "\nDelete record? (Y/N): "):
        all_data.pop(index)
        update_base()
        print("Successfully deleted")
        input("Enter anything to continue...")


def get_index(header):
    while True:
        clear_terminal()
        if header:
            print(header)

        input_str = input_number("Input entry number: ")
        index = -1

        for idx, entry in enumerate(all_data):
            if entry.split()[0] == input_str:
                index = idx

        if index < 0:
            message = f"Entry with number {input_str} not found\n" \
                      + "Hint: use search to find the entry" \
                      + "\nTry again? Y/N: "
            if confirm(message):
                continue

        return index


def export_import():
    pass


def input_entry_data(header):
    if header:
        print(header)
    number = input_number("Enter phone number: ")
    name = input_word("Enter the name: ")
    surname = input_word("Enter the surname: ")
    patron = input_word("Enter the patronymic: ")
    return [number, name, surname, patron]


# def confirm_add_entry(entry):
#     message = "Add the entry? (Y/N): " \
#               + list_to_str(entry, " ")
#     return confirm(message)
#

def append_str(string):
    if not isinstance(string, str):
        print("oops. attempt to append not a string!")
        return False
    with open(file_base, "a", encoding="utf-8") as file:
        file.write(string + "\n")
        file.close()
    return True


def update_base():
    with open(file_base, "w", encoding="utf-8") as file:
        file.write(list_to_str(all_data, "\n"))
        file.close()


def confirm(message):
    while True:
        clear_terminal()
        print(message)
        decision = input().upper()
        if decision == "Y":
            return True
        elif decision == "N":
            return False


def input_number(message):
    while True:
        input_str = input(message).strip()

        if check_number(input_str):
            return input_str


def check_number(num_str):
    # можно было бы заморочиться регулярками, но, но, но
    for c in num_str:
        if not c.isdigit():
            print("Incorrect number input")
            return False
    return True


def input_word(message):
    while True:
        input_str = input(message).strip()

        if check_word(input_str):
            return input_str


def check_word(input_str):
    for c in input_str:
        if not c.isalpha():
            print("Incorrect word input")
            return False
    return True


def match_entries(string):
    matches = []
    if not string:
        return matches
    for entry in all_data:
        if string in entry:
            matches.append(entry)
    return matches


def main_menu():
    while True:
        read_records()
        clear_terminal()

        quantity = len(all_data)
        if quantity == 0:
            note = "no entries"
        elif quantity == 1:
            note = "1 entry"
        else:
            note = f"{quantity} entries"

        answer = input(f"Phone book ({note}):\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Change a record\n"
                       "5. Delete a record\n"
                       "6. Export/Import\n"
                       "7. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_record()
            case "3":
                search_record()
            case "4":
                change_record()
            case "5":
                delete_record()
            case "6":
                export_import()
            case "7":
                return
            case _:
                print("Try again!\n")


def clear_terminal():
    system("cls")


main_menu()
