# Дан символ C. Вывести его код(то есть номер в кодовой таблице)
while True:
    C = input('Введите один символ: ')
    if len(C) == 1:
        break
    print()
print(ord(C))
