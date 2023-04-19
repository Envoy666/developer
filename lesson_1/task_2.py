"""
Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
"""

# полагаем, что будут вводиться только цифры
inputStr = input("Введите число: ")

while len(inputStr) != 3:
    print("Число должно быть трехзначным!")
    inputStr = input("Повторите ввод числа: ")

number = int(inputStr)
summ: int = 0
while number != 0:
    summ += number % 10
    number //= 10

print("Сумма цифр:", str(summ))
