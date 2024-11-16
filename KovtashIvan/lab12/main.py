# Абстракція кольору
class Color:
    def fill_color(self):
        pass

# Конкретні реалізації кольорів
class RedColor(Color):
    def fill_color(self):
        return "червоний"

class BlueColor(Color):
    def fill_color(self):
        return "синій"

class GreenColor(Color):
    def fill_color(self):
        return "зелений"

# Абстракція форми
class Shape:
    def __init__(self, color):
        self.color = color
    
    def draw(self):
        pass

# Конкретні реалізації форм
class Circle(Shape):
    def draw(self):
        return f"Круг {self.color.fill_color()} кольору"

class Square(Shape):
    def draw(self):
        return f"Квадрат {self.color.fill_color()} кольору"

class Triangle(Shape):
    def draw(self):
        return f"Трикутник {self.color.fill_color()} кольору"

# Демонстрація роботи
if __name__ == "__main__":
    # Створюємо кольори
    red = RedColor()
    blue = BlueColor()
    green = GreenColor()
    
    # Створюємо різні форми з різними кольорами
    red_circle = Circle(red)
    blue_square = Square(blue)
    green_triangle = Triangle(green)
    
    # Виводимо результати
    print(red_circle.draw())
    print(blue_square.draw())
    print(green_triangle.draw())
    
    # Демонструємо гнучкість - створюємо нові комбінації
    blue_circle = Circle(blue)
    green_square = Square(green)
    red_triangle = Triangle(red)
    
    print("\n" + "="*50 + "\n")
    
    print(blue_circle.draw())
    print(green_square.draw())
    print(red_triangle.draw())
