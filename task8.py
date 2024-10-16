class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass
        

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Square(Shape):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

circle = Circle("red", 5)
print("Circle area:", circle.area())
print("Circle perimeter:", circle.perimeter())

square = Square("blue", 4)
print("Square area:", square.area())
print("Square perimeter:", square.perimeter())
