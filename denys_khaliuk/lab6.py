class Person:
    count = 0

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

        Person.count += 1

    def generate_description(self):
        return f"name: {self.name}, age: {self.age}, gender: {self.gender}"

person1 = Person("Andriy", 18, "Starosta")
person2 = Person("Denys", 19, "Male")

print(person1.generate_description())
print(person2.generate_description())

print("к-сть людей:", Person.count)
