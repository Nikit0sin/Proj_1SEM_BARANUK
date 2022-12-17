# Даны два целых числа A и B(A < B).
# Вывести в порядке возрастания все целые числа, расположенные между A и B (включая сами числа A и B),
# а также количество N этих чисел.

A = input('Введите число: ')
while type(A) != int:
    try:
        A = int(A)
    except ValueError:
        print('Число введено неправильно')
        A = input("Введите число: ")
B = input('Введите число: ')
while type(B) != int:
    try:
        B = int(B)
    except ValueError:
        print('Число введено неправильно')
        B = input("Введите число: ")
print('A = ', A)
print('B = ', B)
N = 0
for i in range(A, B+1, 1):
    N += 1
    print(i, " : ", N)
print("N = ", N)
