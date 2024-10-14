class Shape:
    def clone(self):
        new_obj = self.__class__.__new__(self.__class__)
        new_obj.__dict__.update(self.__dict__)
        return new_obj

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"Circle with radius: {self.radius}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle with width: {self.width} and height: {self.height}"

circle1 = Circle(5)
circle2 = circle1.clone()
rectangle1 = Rectangle(10, 20)
rectangle2 = rectangle1.clone()

circle2.radius = 7
rectangle2.width = 15

print(circle1)    # Виведе: 5
print(circle2)    # Виведе: 7
print(rectangle1) # Виведе: 20
print(rectangle2) # Виведе: 20
