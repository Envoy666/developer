"""
Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
(т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры.
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”,
если с ритмом все не в порядке
"""


def completion(_poem):
    if len(_poem) == 0:
        return "пустая строка"

    vowel_set = {'а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}
    index = 0
    phrase_rhythm = [0]
    a_idx_low = ord('a')
    z_idx_low = ord('z')
    a_idx_up = ord('A')
    z_idx_up = ord('Z')
    for idx, char in enumerate(_poem):
        if a_idx_low <= ord(char) <= z_idx_low or a_idx_up <= ord(char) <= z_idx_up:
            return "функция не расчитана на работу с латиницей"
        if char in vowel_set:
            phrase_rhythm[index] += 1
        elif char == ' ' and idx != len(_poem) - 1:
            phrase_rhythm += [0]
            index += 1

    if len(phrase_rhythm) == 1:
        return "похоже, что в стихотворении только одно слово?"

    else:
        is_rhythmic = True
        for rhythm in phrase_rhythm:
            if rhythm != phrase_rhythm[0]:
                is_rhythmic = False
                break

        if is_rhythmic:
            return "Парам пам-пам"
        else:
            return "Пам парам"


poem = ""
while len(poem) == 0:
    poem = input("Введите стихотворение: ")
# poem = пара-ра-рам рам-пам-папам па-ра-па-да

print(completion(poem))
