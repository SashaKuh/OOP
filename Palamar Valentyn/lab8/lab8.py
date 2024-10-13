# Батьківський клас
class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        """Метод, що відображає рух об'єкта."""
        print(f"{self.name} is moving...")

# Дочірній клас 1
class Car(Vehicle):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def honk(self):
        """Метод, що відображає дію вдарення в клаксон."""
        print(f"{self.name} honks!")

# Дочірній клас 2
class Plane(Vehicle):
    def __init__(self, name, airline):
        super().__init__(name)
        self.airline = airline

    def fly(self):
        """Метод, що відображає політ об'єкта."""
        print(f"{self.name} is flying!")

# Використання методів об’єктів-представників іншого дочірнього класу
class Boat:
    def __init__(self, name):
        self.name = name

    def sail(self):
        """Метод, що відображає плавання об'єкта."""
        print(f"{self.name} is sailing!")

car = Car("Toyota", "Red")
car.move()  # Output: Toyota is moving...
car.honk()  # Output: Toyota honks!

plane = Plane("Boeing", "Emirates")
plane.move()  # Output: Boeing is moving...
plane.fly()  # Output: Boeing is flying!

boat = Boat("Titanic")
boat.sail()  # Output: Titanic is sailing!

# Перевірка належності до класів
print(isinstance(boat, Vehicle))  # Output: False
print(issubclass(Boat, Vehicle))  # Output: False
