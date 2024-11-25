from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class AreaCalculator:
    def calculate_area(self, shape: Shape):
        return shape.area()


# Використання
circle = Circle(5)
rectangle = Rectangle(10, 5)
triangle = Triangle(8, 4)

calculator = AreaCalculator()
print(f"Area of Circle: {calculator.calculate_area(circle)}")
print(f"Area of Rectangle: {calculator.calculate_area(rectangle)}")
print(f"Area of Triangle: {calculator.calculate_area(triangle)}")
