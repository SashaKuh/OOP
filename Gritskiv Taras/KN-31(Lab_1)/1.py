class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Автомобіль їде по дорозі")

class Plane(Vehicle):
    def move(self):
        print("Літак летить по небу")

class Ship(Vehicle):
    def move(self):
        print("Корабель пливе по морю")

class VehicleFactory:
    def create_vehicle(self, vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "plane":
            return Plane()
        elif vehicle_type == "ship":
            return Ship()
        else:
            raise ValueError("Невідомий тип транспортного засобу")

# Використання фабрики
factory = VehicleFactory()
car = factory.create_vehicle("car")
plane = factory.create_vehicle("plane")
ship = factory.create_vehicle("ship")

car.move()
plane.move()
ship.move()