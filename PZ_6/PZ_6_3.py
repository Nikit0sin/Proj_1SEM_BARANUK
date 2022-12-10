# Дан массив A размера N и целые числа K и L (1 ≤ K < L ≤ N).
# Переставить в обратном порядке элементы массива, расположенные между элементами AK и AL, не включая эти элементы.
import random
N = random.randrange(2, 19)
L = random.randrange(2, N + 1)
K = random.randrange(1, L)

A = [i + 1 for i in range(N)]
print("N:", N)
print("L:", L)
print("K:", K)
print("Список A:\n", A)
M = (L - K + 1) // 2
print("M:", M)
i = 1
while i < M:
    A[K - 1 + i], A[L - 1 - i] = A[L - 1 - i], A[K - 1 + i]
    i += 1

print("Новый список A:\n", A)
