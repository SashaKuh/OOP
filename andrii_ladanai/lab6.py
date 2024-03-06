class Car:
    total_cars = 0

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.full_description = f"{year} {make} {model}"

        Car.total_cars += 1

    def generate_description(self):
        return f"{self.color} {self.full_description}"

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars

# Використання лічильника створених об'єктів
print("Total cars:", Car.get_total_cars())  # Виведе: Total cars: 0

car1 = Car("Toyota", "Camry", 2022, "Blue")
print(car1.generate_description())
print("Total cars:", Car.get_total_cars())  # Виведе: Total cars: 1
