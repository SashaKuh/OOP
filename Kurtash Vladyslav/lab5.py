class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def scream(self):
        print("Screaming!")

person = Person("Vlad", 100)
person.scream()  #Output: Screaming!
