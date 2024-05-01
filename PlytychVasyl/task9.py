class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def move(self):
        pass


    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

class Car(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

    def move(self):
        return "Car is driving."

class Plane(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

    def move(self):
        return "Plane is flying."

class Boat(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

    def move(self):
        return "Boat is sailing."

# Функція, яка використовує поліморфізм
def travel(vehicle):
    return vehicle.move()

car = Car("Toyota", "Corolla", 2010)
plane = Plane("Boeing", "747", 1995)
boat = Boat("Yamaha", "SX210", 2018)

print(car)        # Викликається __str__
print(travel(car))    # Викликається move() для Car
print(travel(plane))  # Викликається move() для Plane
print(travel(boat))   # Викликається move() для Boat
