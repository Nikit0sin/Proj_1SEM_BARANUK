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
