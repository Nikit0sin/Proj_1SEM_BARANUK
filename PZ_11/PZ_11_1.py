# Средствами языка Python сформировать текстовый файл (.txt),
# содержащий новый текстовый файл (.txt) следующего вида,
# предварительно выполнив требуемую обработку элементов:
# Исходные данные:
# Количество элементов:
# Отрицательные нечетные элементы:
# Сумма отрицательных нечетных элементов:
# Среднее арифметическое отрицательных нечетных элементов:
num = '-10 -9 -8 -7 -6 -5 -4 -3 -2 -1 2 3 4 5 6 7 8 9 10'
new = open('new.txt', 'w')
new.writelines(num)
new.close()

openf = open('new.txt')
read = openf.read().split(' ')
new.close()

odd = open('new.txt')
summ = 0
av_value = []
for i in range(len(read)):
    read[i] = int(read[i])
    if read[i] < 0 and read[i] % 2 != 0:
        av_value.append(read[i])
        summ += read[i]
        av_value_len = summ / len(av_value)

final = open('final.txt', 'w')
final_write = ('Исходные данные: ', num, '\n', 'Количество элементов: ', str(len(read)), '\n',
               'Отрицательные нечётные числа: ', str(av_value), '\n', 'Сумма отрицательных нечётных чисел: ',
               str(summ), '\n', 'Среднее арифметическое отрицательных нечетных элементов: ', str(av_value_len))
final.writelines(final_write)
final.close()
