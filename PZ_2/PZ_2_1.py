# Известно, что X кг конфет стоит A рублей. Определить, сколько стоит 1 кг и Y кг этих же конфет
a = input('Введите целое число: ')
x = input('Введите целое число: ')
y = input('Введите целое число: ')
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print('Неправильно')
        a = input('Введите целое число: ')
while type(x) != int:
    try:
        x = int(x)
    except ValueError:
        print('Неправильно')
        x = input('Введите целое число: ')
while type(y) != int:
    try:
        y = int(y)
    except ValueError:
        print('Неправильно')
        y = input('Введите целое число: ')
kg1 = a/x
kg_y = kg1*y
print(kg1)
print(kg_y)
