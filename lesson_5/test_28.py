"""
Задача 28: Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

*Пример:*

2 2
    4
"""


def summ(a, b):
    if b == 0:
        return a
    return 1 + summ(a, b - 1)


_a, _b = [int(x) for x in input("Введите числa: ").split()]
print(summ(_a, _b))


