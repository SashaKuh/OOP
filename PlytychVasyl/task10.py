class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
print(circle.area)  
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

    @name.deleter
    def name(self):
        del self._name


person = Person("Alice")
print(person.name)  # Викликаємо getter
person.name = "Bob"  # Викликаємо setter
print(person.name)
del person.name  # Викликаємо deleter
