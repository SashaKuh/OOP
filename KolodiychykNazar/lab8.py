#Використання властивостей батьківського класу у дочірньому класi
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        super().speak()  
        print(f"{self.name} barks")

dog = Dog("Buddy", "Labrador")
dog.speak()

#Створення класу, який успадковує властивості від іншого класу
class Shape:
    def __init__(self, color):
        self.color = color

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

# Використання класу-нащадка
circle = Circle("Red", 5)
print("Color of the circle:", circle.color)
