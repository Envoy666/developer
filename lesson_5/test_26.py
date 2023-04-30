"""
Задача 26: Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
"""


def power(a, b):
    if b == 1:
        return a
    else:
        if b > 0:
            return a * power(a, b - 1)
        else:
            return power(a, b + 1) / a


_a = int(input("Введите число: "))
_b = int(input("Введите степень: "))

if _a == 0 and _b == 0:
    print("0 в степени 0 является неопределенностью")
else:
    print(power(_a, _b))
