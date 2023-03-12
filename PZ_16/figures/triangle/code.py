import math


def triange_perimeter():
    per = a + b + c
    return per


def triangle_area():
    p = (a + b + c)/2
    ar = math.sqrt(p + (p - a) + (p - b) + (p - c))
    return ar


a = 7
b = 2
c = 8
print(triangle_area())
