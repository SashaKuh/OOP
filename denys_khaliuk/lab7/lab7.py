#Альтернативні конструктори:
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @classmethod
    def from_(cls, name, birth_year, gender):
        age = 2024 - birth_year
        return cls(name, age, gender)

person = Person.from_("Andriy", 2005, "Starosta")
print(person.name, person.age, person.gender)

#Метод класу, який працює зі змінними класу:
class Person:
    count = 0

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Person.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

print(Person.get_count())
person1 = Person("Andriy", 18, "Starosta")
person2 = Person("Denys", 19, "Male")
print(Person.get_count())

#Альтернативний конструктор за допомогою методу класу:
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @classmethod
    def from_string(cls, string):
        name, age, gender = string.split(',')
        return cls(name, int(age), gender)

person4 = Person.from_string("Andriy,19,Starosa")
print(person4.name, person4.age, person4.gender)

#Статичний метод:

class Stat:
    @staticmethod
    def add(x, y):
        return x + y

print(Stat.add(5, 3))




