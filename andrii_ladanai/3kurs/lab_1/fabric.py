class Vehicle:
    def __init__(self, id, owner_name, amount, section_number):
        self.id = id
        self.owner_name = owner_name
        self.amount = amount
        self.section_number = section_number


class Car(Vehicle):
    def __init__(self, id, owner_name, car_model, amount, section_number):
        super().__init__(id, owner_name, amount, section_number)
        self.car_model = car_model

    @classmethod
    def from_input(cls):
        id = input("Введіть ваш id ")
        owner_name = input("Введіть ваше ім'я ")
        car_model = input("Введіть модель автомобіля ")
        amount = input("Введіть кількість годин, які ви плануєте паркуватися ")
        section_number = input("Введіть номер секції, де ви плануєте паркуватися ")
        return cls(id=id, owner_name=owner_name, car_model=car_model, amount=amount, section_number=section_number)


class Motorcycle(Vehicle):
    def __init__(self, id, owner_name, motorcycle_model, amount, section_number):
        super().__init__(id, owner_name, amount, section_number)
        self.motorcycle_model = motorcycle_model

    @classmethod
    def from_input(cls):
        id = input("Введіть ваш id ")
        owner_name = input("Введіть ваше ім'я ")
        motorcycle_model = input("Введіть модель мотоцикла ")
        amount = input("Введіть кількість годин, які ви плануєте паркуватися ")
        section_number = input("Введіть номер секції, де ви плануєте паркуватися ")
        return cls(id=id, owner_name=owner_name, motorcycle_model=motorcycle_model, amount=amount, section_number=section_number)


class VehicleFactory:
    def create_vehicle(self, vehicle_type):
        if vehicle_type == "Car":
            return Car.from_input()
        elif vehicle_type == "Motorcycle":
            return Motorcycle.from_input()
        else:
            raise ValueError("Неправильний тип транспортного засобу")


factory = VehicleFactory()


def choice(factory=None):
    while True:
        x = str(input('Виберіть 1 - якщо ви хочете записати дані про автомобіль\n'
                      'Виберіть 2 - якщо ви хочете записати дані про мотоцикл\n'
                      'Якщо ви хочете вийти, виберіть - 3\n'))
        if "1" == x:
            print("Ви вибрали автомобіль, введіть дані")
            factory = VehicleFactory()
            car = factory.create_vehicle("Car")
            break
        elif '2' == x:
            print("Ви вибрали мотоцикл, введіть дані")
            motorcycle = factory.create_vehicle("Motorcycle")
            break
        elif x == '3':
            break
        else:
            print("Такого транспортного засобу ще не додано")

choice()


