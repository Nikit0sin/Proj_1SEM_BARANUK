# Из предложенного текстового файла (text18-1.txt) вывести на экран его содержимое,
# количество букв в верхнем регистре. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно поставив последнюю строку между первой и второй.
t = 0
d = 0
for i in open('text18-1.txt', encoding='UTF-8'):
    print(i, end='')
    t += 1
    for up in i:
        if up in 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ':
            d += 1
print(end='\n')
print('Количество строк: ', d)
f1 = open('text18-1.txt', encoding='UTF-8')
t = f1.readlines()
f1.close()
t.insert(1, t[6])
t.insert(2, '\n')
f2 = open('text18-2.txt', 'w')
f2.writelines(t)
f2.close()
