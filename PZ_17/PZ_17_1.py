# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Создайте класс «Круг», который имеет атрибут радиуса и методы для вычисления площади, длины окружности и диаметра.
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def circumference(self):
        return 2 * 3.14 * self.radius

    def diameter(self):
        return 2 * self.radius


resh = Circle(13)
print("Площадь круга:", resh.area())
print("Длина окружности:", resh.circumference())
print("Диаметр:", resh.diameter())
