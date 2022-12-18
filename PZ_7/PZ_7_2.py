# Дана строка, содержащая латинские буквы и скобки трех видов: «()», «[]», «{}».
# Если скобки расставлены правильно (то есть каждой открывающей соответствует закрывающая скобка того же вида),
# то вывести число 0.
# В противном случае вывести или номер позиции, в которой расположена первая ошибочная скобка,
# или, если закрывающих скобок не хватает, число – 1.
def cheaksequence(string):
    stack = []

    brackets = [
        ("(", ")"),
        ("[", "]"),
        ("{", "}")
    ]

    for c in string:
        for openBracket, closeBracket in brackets:
            if c == openBracket:
                stack.append(openBracket)
                break
            elif c == closeBracket:
                if (stack == []) or (openBracket != stack.pop()):
                    return 0
                break
    return stack == []


string = input("Введите строку: ")


print("0" if cheaksequence(string) else "1")
