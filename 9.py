class Point:
    color = 'red'
    circle = 2

# print(Point.color)
# print(Point.circle)
# print(Point.__dict__)

pointOne = Point()
# print(pointOne.circle)
# print(pointOne.__dict__)

pointTwo = Point()
# print(pointTwo.color)
# print(pointTwo.__dict__)

Point.circle = 3
# print(Point.circle)
# print(pointOne.circle)

pointOne.color = 'green'
# print(pointOne.color)
# print(pointTwo.color)

Point.hiddens = False
Point.inner = True
# print(Point.__dict__)
# print(pointOne.hiddens)
# print(pointTwo.inner)

# print(pointOne.__dict__)
# print(pointTwo.__dict__)
# pointOne.like = True
# print(pointOne.__dict__)

# del Point.hiddens
# print(Point.__dict__)

# print(getattr(pointTwo, 'hiddens', False))
# print(getattr(pointTwo, 'inner', False))

# print(hasattr(Point, 'circle'))

# if hasattr(Point, 'inner'):
#     del Point.inner
# print(getattr(Point, 'inner', False))

# pointOne.like = True
# print(pointOne.like)

pointOne.circle = 5
# print(pointOne.circle)

# del pointOne.circle
# print(Point.hiddens == False)
# Point.inner = True

# def set_coords(self, x=0, y=0):
#     print("вызов метода set_coords для " + str(self))
#     self.x = x
#     self.y = y

# pointOne = Point()

# pointOne.set_coords(10, 20)
# print(pointOne.__dict__)


