class Point:
    def __init__(self, x=0, y=0):
        print("Вызов метода __init__ для " + str(self))
        self.x = x
        self.y = y


    def __del__(self):
        print("Удаление экземпляра: " + str(self))

    
    def get_coords(self):
        print("Вызов метода get_coords для " + str(self))
        return self.x, self.y
    
