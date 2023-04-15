"""
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд
и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый,
т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no

"""

inputStr = input("Введите 6-значное число: ")
while len(inputStr) != 6:
    print("Число должно быть 6-значным!")
    inputStr = input("Повторите ввод: ")

leftStr = inputStr[:3]
rightStr = inputStr[3:]

"""
#  для чисел произвольной длины
inputStr = input("Введите число с четным количеством цифр: ")

while len(inputStr) % 2 != 0:
    print("Количество цифр в числе должно быть четным!")
    inputStr = input("Повторите ввод: ")

half = len(inputStr) // 2
leftStr = inputStr[:half]
rightStr = inputStr[half:]
"""

print(leftStr, rightStr)

leftNum = int(leftStr)
rightNum = int(rightStr)

leftSumm = 0
rightSumm = 0

while leftNum != 0 or rightNum != 0:
    leftSumm += leftNum % 10
    rightSumm += rightNum % 10
    leftNum //= 10
    rightNum //= 10

if leftSumm == rightSumm:
    print("Счастливый билет!")
else:
    print("Обычный билет")
