from abc import ABC, abstractmethod
from random import randrange
from typing import List

class Vehicle:
    """
    Базовий клас для транспортних засобів.
    """
    def __init__(self, id, owner_name, amount, section_number):
        self.id = id
        self.owner_name = owner_name
        self.amount = amount
        self.section_number = section_number

class Car(Vehicle):
    """
    Клас для автомобілів.
    """
    def __init__(self, id, owner_name, car_model, amount, section_number):
        super().__init__(id, owner_name, amount, section_number)
        self.car_model = car_model

    @classmethod
    def from_input(cls):
        id = input("Введіть ваш id: ")
        owner_name = input("Введіть ваше ім'я: ")
        car_model = input("Введіть модель автомобіля: ")
        amount = input("Введіть кількість годин, які ви плануєте паркуватися: ")
        section_number = input("Введіть номер секції, де ви плануєте паркуватися: ")
        return cls(id=id, owner_name=owner_name, car_model=car_model, amount=amount, section_number=section_number)

class Motorcycle(Vehicle):
    """
    Клас для мотоциклів.
    """
    def __init__(self, id, owner_name, motorcycle_model, amount, section_number):
        super().__init__(id, owner_name, amount, section_number)
        self.motorcycle_model = motorcycle_model

    @classmethod
    def from_input(cls):
        id = input("Введіть ваш id: ")
        owner_name = input("Введіть ваше ім'я: ")
        motorcycle_model = input("Введіть модель мотоцикла: ")
        amount = input("Введіть кількість годин, які ви плануєте паркуватися: ")
        section_number = input("Введіть номер секції, де ви плануєте паркуватися: ")
        return cls(id=id, owner_name=owner_name, motorcycle_model=motorcycle_model, amount=amount, section_number=section_number)

class VehicleFactory:
    """
    Фабрика для створення транспортних засобів.
    """
    def create_vehicle(self, vehicle_type):
        if vehicle_type == "Car":
            return Car.from_input()
        elif vehicle_type == "Motorcycle":
            return Motorcycle.from_input()
        else:
            raise ValueError("Неправильний тип транспортного засобу")

def choice():
    factory = VehicleFactory()  # Фабрика ініціалізується один раз
    while True:
        x = input('Виберіть 1 - якщо ви хочете записати дані про автомобіль\n'
                  'Виберіть 2 - якщо ви хочете записати дані про мотоцикл\n'
                  'Якщо ви хочете вийти, виберіть - 3\n')
        if x == "1":
            print("Ви вибрали автомобіль, введіть дані:")
            car = factory.create_vehicle("Car")
            print(f"Автомобіль зареєстровано: ID - {car.id}, Власник - {car.owner_name}, Модель - {car.car_model}")
        elif x == '2':
            print("Ви вибрали мотоцикл, введіть дані:")
            motorcycle = factory.create_vehicle("Motorcycle")
            print(f"Мотоцикл зареєстровано: ID - {motorcycle.id}, Власник - {motorcycle.owner_name}, Модель - {motorcycle.motorcycle_model}")
        elif x == '3':
            print("Програма завершена.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

choice()
