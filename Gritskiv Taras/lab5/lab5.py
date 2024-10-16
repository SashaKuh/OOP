from math import sqrt
class Rectangle():
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def __str__(self):
        return f"Із даного прямокутника зі сторонами {self.length} та {self.width} ми можемо дізнатись наступні данні: \nПериметр: {self.perimeter()}\nПлоща:{self.area()}\nДовжина діагоналей:{self.diagonal()}\nРадіус описаного кола:{self.radius()}\n"
    def perimeter(self):
        return 2*(int(self.length)+int(self.width))
    def area(self):
        return int(self.width)*int(self.length)
    def diagonal(self):
        return int(sqrt(int(self.width)**2+int(self.length)**2))
    def radius(self):
        return int(self.perimeter()/2)

my_data=Rectangle(3,4)
print(my_data)
class Square(Rectangle):
    def __init__(self,length):
        self.length=int(length)
    def __str__(self):
        return f"Із даного прямокутника зі сторонами довжиною по {self.length} ми можемо дізнатись наступні данні: \nПериметр: {self.perimeter()}\nПлоща: {self.area()}\nДовжина діагоналей: {self.diagonal()}\nРадіус описаного кола: {self.radius_of_the_circle()}\nРадіус вписаного кола: {self.radius_of_the_inscribed_circle()}"
    def perimeter(self):
        return int(self.length*4)
    def area(self):
        return int(self.length**2)
    def diagonal(self):
        return int(self.length*sqrt(2))
    def radius_of_the_circle(self):
        return int(self.diagonal()/2)
    def radius_of_the_inscribed_circle(self):
        return int(self.length/2)

my_data_of_square=Square(4)
print(my_data_of_square)