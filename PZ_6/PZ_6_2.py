# Дан массив размера N
# Найти номера тех элементов массива, которые больше своего правого соседа, и количество таких элементов.
# Найденные номера выводить в порядке их возрастания.

import random

N = random.randrange(2, 11)
print("N = ", N)
a = [random.randrange(1, 11) for i in range(N)]
print(a)
c = 0
for i in range(0, len(a) - 1):
    if a[i] > a[i + 1]:
        c += 1
        print(i, end="; ")
print()
print("Количество:", c)
