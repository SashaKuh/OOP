class Animal:
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Гав")


class Cat(Animal):
    def sound(self):
        print("Мяу")


class Cow(Animal):
    def sound(self):
        print("Мууу")


class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        elif animal_type == "cow":
            return Cow()
        else:
            raise ValueError("Невідомий тип тварини")


factory = AnimalFactory()


dog = factory.create_animal("dog")
cat = factory.create_animal("cat")
cow = factory.create_animal("cow")


dog.sound() 
cat.sound()  
cow.sound()  