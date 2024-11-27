class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


def print_area(rectangle):
    print(f"Area: {rectangle.area()}")


rectangle = Rectangle(10, 5)
square = Square(5)

print_area(rectangle) 
print_area(square)    
