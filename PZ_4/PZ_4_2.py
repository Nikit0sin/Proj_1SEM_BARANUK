import random
A, B = [random.randrange(1, 21) for i in range(0, 2)]
C = random.randint(1, min(A, B))
print("A = {0}, B = {1}, C = {2}".format(A, B, C))
a = int(A / C)
b = int(B / C)
print("Площадь прямоугольника:", A * B)
print("Площадь квадрата:", C * C)
print("Количество квадратов на прямоугольнике:", a * b)
print("Площадь незанятой части прямоугольника:", A * B - a * b * C * C)
A1 = A
n_A = 0
while A1 >= C:
    A1 -= C
    n_A += 1
B1 = B
n_B = 0
while B1 >= C:
    B1 -= C
    n_B += 1
k = 0
i = 0
while i < n_A:
    i += 1
    j = 0
    while j < n_B:
        j += 1
        k += 1
print(n_A, ":", n_B)
print("Количество квадратов на прямоугольнике:", k)
