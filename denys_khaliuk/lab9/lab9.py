class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "woof"

class Cat(Animal):
    def make_sound(self):
        return "meow"

class Bird(Animal):
    def make_sound(self):
        return "kyky"

dog = Dog()
cat = Cat()
bird = Bird()

print(dog.make_sound())
print(cat.make_sound())
print(bird.make_sound())
