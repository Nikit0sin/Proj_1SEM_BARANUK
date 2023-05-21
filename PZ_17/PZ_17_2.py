# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Создайте класс "Фигура", который содержит метод расчета площади фигуры.
# Создайте классы "Квадрат" и "Прямоугольник", которые наследуются от класса
# "Фигура". Каждый класс должен иметь метод расчета площади собственной фигуры.
class Shape:
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


my_square = Square(4)
my_rectangle = Rectangle(2, 6)

print("Площадь квадрата:", my_square.area())
print("Площадь прямоугольника:", my_rectangle.area())
