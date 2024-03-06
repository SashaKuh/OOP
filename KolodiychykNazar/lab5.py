#Оголошення класів
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} гавкає!")

#Створення об'єктів
my_dog = Dog("Барон", 4)

#Поняття змінної
class Dog:
    species = "Собака"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} гавкає!")

print(Dog.species) 

my_dog = Dog("Барон", 4)
print(my_dog.name)  

#Поняття методів 
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} гавкає!")
my_dog = Dog("Барон", 4)
my_dog.bark() 

#Розв'язання заданої задачі
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
my_rectangle = Rectangle(5, 3)

print("Площа:", my_rectangle.area())
print("Периметр:", my_rectangle.perimeter())


