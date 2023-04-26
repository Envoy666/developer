"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
"""

from random import randint

N = int(input("Введите количество элементов в массиве: "))

while N < 1:
    print("Число не может быть меньше 1!")
    N = int(input("Повторите ввод: "))

rand_list = [randint(-10, 10) for i in range(0, N)]
print(*rand_list)

X = int(input("Введите требуемое значение: "))

close = rand_list[0]
delta = abs(X - close)

for i in range(1, N):
    new_delta = abs(X - rand_list[i])
    if new_delta < delta:
        delta = new_delta
        close = rand_list[i]

print("Число %d - ближайшее к значению %d" % (close, X))
