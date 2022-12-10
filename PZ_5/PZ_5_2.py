# Описать функцию PowerA234(параметры), вычисляющую вторую, третью и четвертую степень числа А и
# возвращающую эти степени соответственно в переменные B, C и D.
# С помощью этой функции найти вторую, третью и четвертую степень пяти данных чисел.
import random


def PowerA234(a, b):
    b[0] = a * a
    b[1] = b[0] * a
    b[2] = b[1] * a
    return


a = random.randrange(-10, 10)
b = [None] * 3
PowerA234(a, b)
print('A = ', a)
print('B = ', b)
a = random.uniform(-10, 10)
PowerA234(a, b)
print('A = ', a)
print('B = ', b)
