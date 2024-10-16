class Animal:
    def __init__(self, species, age):
        self.species = species
        self._age = age  # Інкапсуляція: змінна тепер є приватною

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, int) and value >= 0:
            self._age = value
        else:
            raise ValueError("Вік має бути не від'ємним цілим числом.")

    def del_age(self):
        print(f"Видалення віку для тварини '{self.species}'")
        self._age = None

try:
    animal = Animal("Dog", 5)
    print(animal.age)  # Використання getter'а

    animal.age = 7  # Використання setter'а
    print(animal.age)

    del animal.age  # Використання deleter'а
    print(animal.age)  # None або дефолтне значення, яке встановлено deleter'ом

    animal.age = -3  # Спроба встановити недопустиме значення
except ValueError as e:
    print(e)
