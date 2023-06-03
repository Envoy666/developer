"""
Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
которые должны быть распечатаны.
"""


def print_operation_table(operation, num_rows, num_columns):
    if num_rows > 0 and num_columns > 0:
        table = [[operation(i, j) for j in range(1, num_columns + 1)]
                 for i in range(1, num_rows + 1)]
        for row in table:
            print(*row, sep=' ')
    else:
        print("Числа должны быть больше 0")


print_operation_table(lambda x, y: x * y, 5, 6)
