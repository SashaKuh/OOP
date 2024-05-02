class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        return "woof"


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color

    def chase_mouse(self, mouse):
        return f"{self.name} is chasing {mouse}!"

dog = Dog("Buddy", "Golden Retriever")
print(dog.name)
print(dog.species)
print(dog.breed)
print(dog.make_sound())

cat = Cat("Whiskers", "Gray")
print(cat.name)
print(cat.species)
print(cat.color)
print(cat.make_sound())
print(cat.chase_mouse("a mouse"))

print(isinstance(dog, Dog))  # True
print(isinstance(dog, Animal))  # True

print(issubclass(Dog, Animal))  # True
print(issubclass(Cat, Animal))  # True

