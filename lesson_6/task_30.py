"""
Задача 30: Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки
"""


def progression(items_list, prev_item, delta, count):
    if count == 0:
        return items_list
    else:
        next_item = prev_item + delta
        items_list = items_list + [next_item]
        return progression(items_list, next_item, delta, count - 1)


n = int(input("Введите первый элемент: "))
m = int(input("Введите разность между элементами: "))
l = int(input("Введите количество элементов: "))


print(*progression([], n, m, l))
