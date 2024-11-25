# Брудний код
class Automob:
    def __init__(self, motor):
        self.motor = motor

    def turn_on(self):
        if self.motor == "Electric":
            return "Starting electric engine..."
        elif self.motor == "Petrol":
            return "Starting petrol engine..."
        else:
            return "Starting unknown engine type"


# Після рефакторингу
from abc import ABC, abstractmethod


# Базовий клас для автомобілів
class Car(ABC):
    @abstractmethod
    def start_engine(self):
        pass


# Клас для електромобілів
class ElectricCar(Car):
    def start_engine(self):
        return "Starting electric engine..."


# Клас для бензинових автомобілів
class PetrolCar(Car):
    def start_engine(self):
        return "Starting gasoline engine..."


# Використання
print(ElectricCar().start_engine())
print(PetrolCar().start_engine())
