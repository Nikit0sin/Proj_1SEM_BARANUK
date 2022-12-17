# Даны координаты точки, не лежащей на координатных осях OX и OY.
# Определить номер координатной четверти, в которой находится данная точка.
print("Введите координаты точки: ")
x = input("x = ")
while type(x) != float:
    try:
        x = float(x)
    except ValueError:
        print('Число введено неправильно')
        x = input("x = ")
y = input("y = ")
while type(y) != float:
    try:
        y = float(y)
    except ValueError:
        print('Число введено неправильно')
        y = input("y = ")
if x > 0 and y > 0:
    print("Точка находится в I четверти")
elif x < 0 and y > 0:
    print("Точка находится в II четверти")
elif x < 0 and y < 0:
    print("Точка находится в III четверти")
elif x > 0 and y < 0:
    print("Точка находится в IV четверти")
