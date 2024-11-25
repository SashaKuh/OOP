class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def animal_name(self):
        return self.name
    def animal_age(self):
        return self.age
    def __str__(self):
        return f"Ім'я  тварини {self.name} а її вік {self.age}"

animal = Animal("Кіт", 7)
print(animal)