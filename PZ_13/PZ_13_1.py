import random

n = 5
m = 5
matr2 = [[random.randint(1, 10) for j in range(m)] for i in range(n)]

matr1 = []

for i in range(1, len(matr2)-1):
    row = []
    for j in range(1, len(matr2[0])-1):
        row.append(matr2[i][j])
    matr1.append(row)

print(matr1)