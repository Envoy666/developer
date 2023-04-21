"""
*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка;
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков;
J, X – 8 очков;
Q, Z – 10 очков.
А русские буквы оцениваются так:
А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
либо только русские буквы.

*Пример:*

ноутбук
    12

"""

# лень-матушка, правда я совершенно не разбираюсь,
# что там "под капотом" у пайтона, поэтому не исключено, что творится полнейший моветон
stringEN = "A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков."
stringRU = "А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков."
stringBoth = stringEN + stringRU
dictionaries = [{}, {}]
dIdx = 0
keys = []
value = -1
two_digits = False
for index, char in enumerate(stringBoth):
    if two_digits: 
        two_digits = False
        continue
    if char.isalpha():
        if char.islower(): continue
        else: keys.append(char)
    elif char.isdigit():
        next_char = stringBoth[index + 1]
        # тут бы рекурсию, на трёх- и более "-значные" числа, а вместо флага two_digits счетчик...
        if next_char.isdigit():
            char += next_char
            two_digits = True
        value = (int(char))
    elif char == ';' or char == '.':
        # можно потом убрать или как-либо обработать
        if value < 0:
            print("oops. something went wrong")
        for i in range(0, len(keys)):
            dictionaries[dIdx][keys[i]] = value
        keys = []
        value = -1
        if char == '.':
            dIdx += 1
            if dIdx > 1:
                break


input_string = input("Введите слово: ").upper()

while True:
    if dictionaries[0].get(input_string[0]) != None:
        correct = dictionaries[0]
        wrong = dictionaries[1]
        break
    elif dictionaries[1].get(input_string[0]) != None:
        correct = dictionaries[1]
        wrong = dictionaries[0]
        break
    else:
        input_string = input("Введено что-то непонятное, повторите ввод слова: ").upper()

summ = 0
for char in input_string:
    cost = correct.get(char)
    if cost == None:
        cost = wrong.get(char)
        if cost != None:
            print("Слово содержит буквы из разных языков!")
        else:
            print("Слово содержит символы, отсутствующие в словарях!")
        summ = 0
        break

    summ += cost

if summ != 0:
    print ("Стоимость слова: ", summ)
