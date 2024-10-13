class Color:
    def get_color(self):
        pass

class RedColor(Color):
    def get_color(self):
        return "Червоний"

class GreenColor(Color):
    def get_color(self):
        return "Зелений"

class BlueColor(Color):
    def get_color(self):
        return "Синій"

class BlackColor(Color):
    def get_color(self):
        return "Чорний"
    
class FFFColor(Color):
    def get_color(self):
        return "Білий"


class Shape:
    def __init__(self, color: Color):
        self.color = color

    def draw(self):
        pass

class CircleShape(Shape):
    def draw(self):
        print(f"Малюю коло кольору {self.color.get_color()}")

class SquareShape(Shape):
    def draw(self):
        print(f"Малюю квадрат кольору {self.color.get_color()}")

class TriangleShape(Shape):
    def draw(self):
        print(f"Малюю трикутник кольору {self.color.get_color()}")

red = RedColor()
green = GreenColor()
blue = BlueColor()
black = BlackColor()
fff = FFFColor()


circle = CircleShape(red)
square = SquareShape(blue)
triangle_green = TriangleShape(green)
triangle_black = TriangleShape(black)
square = SquareShape(fff)

circle.draw()          
square.draw()          
triangle_green.draw()  
triangle_black.draw()  
