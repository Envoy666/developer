"""
Задача 32: Определить индексы элементов массива (списка), значения которых
принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
"""


items_list = [int(i) for i in input("Введите элементы массива: ").split()]
minimum = int(input("Введите минимум: "))
maximum = int(input("Введите максимум: "))
indexes = []
length = len(items_list)
for i in range(0, length):
    if items_list[i] < minimum or items_list[i] > maximum:
        continue

    indexes.append(i)

print(indexes)

