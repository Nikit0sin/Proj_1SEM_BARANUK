# Из текстового файла (writer.txt) выбрать фамилии писателей, посчитать количество фамилий.
# Создать новый файл, в котором выполнить замену слова «роман» на слово «произведение».
import re

openf = open('writer.txt', encoding='UTF-8')
read = openf.read()
openf.close()

surname = re.findall(r"[^\S](\b[А-Я]\w+)\s[А-Я].[А-Я].", read)
surname_surname = re.findall(r"(\b[А-Я-]\w+.[А-Я]\w*)\s[А-Я].[А-Я].", read)

read_roman = re.sub(r"роман\b", 'произведение', read)

print("Фамилии:", surname)
print("Фамилии через дефис:", surname_surname)
print("Количество фамилий:", len(surname))
print("Количество фамилий через дефис:", len(surname_surname))

final = open('final.txt', 'w')
final.writelines(read_roman)
final.close()
