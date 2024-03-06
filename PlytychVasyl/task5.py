class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 100

    def update_year(self, new_year):
        self.year = new_year
        print(f"The car's year has been updated to {self.year}.")

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Mileage: {self.mileage} miles")


my_car = Car("Toyota", "Corolla", 2020)

my_car.update_year(2022)
my_car.display_info()
