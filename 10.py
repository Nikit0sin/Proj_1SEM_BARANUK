class Point:
    color = 'red'
    circle = 2
    def set_coords(self, x=0, y=0):
        print("вызов метода set_coords для " + str(self))
        self.x = x
        self.y = y

    def get_coords(self):
        print("вызов метода get_coords для " + str(self))
        return(self.x, self.y)

pointOne = Point()

# pointOne.set_coords(10, 20)
# print(pointOne.__dict__)

pointOne.set_coords()
print(pointOne.__dict__)