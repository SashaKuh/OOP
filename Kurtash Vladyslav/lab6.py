class Bicycle:
    total_vehicles = 0

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.full_description = f"{year} {make} {model}"

        Bicycle.total_vehicles += 1

    def printDescription(self):
        return f"{self.color} {self.full_description}"

    @classmethod
    def get_total_vehicles(cls):
        return cls.total_vehicles

print("Total bicycles:", Bicycle.get_total_vehicles())  # Output: Total bicycles: 0

bicycle_1 = Bicycle("Bicycle1", "Model1", 2000, "White")
print(bicycle_1.printDescription())
print("Total bicycles:", Car.get_total_vehicles())  # Output: Total bicycles: 1
