# Базовий клас
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} говорить")

# Підклас, який успадковує властивості та методи від базового класу Animal
class Dog(Animal):
    def __init__(self, name, breed):
        # Викликаємо конструктор базового класу для ініціалізації властивостей, спільних з базовим класом
        super().__init__(name)
        self.breed = breed

    # Перевизначення методу speak() для підкласу Dog
    def speak(self):
        print(f"{self.name} гавкає")

# Підклас, який успадковує властивості та методи від базового класу Animal
class Cat(Animal):
    def __init__(self, name, color):
        # Викликаємо конструктор базового класу для ініціалізації властивостей, спільних з базовим класом
        super().__init__(name)
        self.color = color

    # Перевизначення методу speak() для підкласу Cat
    def speak(self):
        print(f"{self.name} муркотить")

# Створення об'єктів різних класів
dog = Dog("Рекс", "Джек-рассел тер'єр")
cat = Cat("Вася", "Сірий")

# Виклик методу speak() для кожного об'єкту
dog.speak()  # Результат: Рекс гавкає
cat.speak()  # Результат: Вася муркотить
