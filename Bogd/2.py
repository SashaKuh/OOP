class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def get_make(self):
        return self.__make

    def set_make(self, make):
        self.__make = make

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year


car1 = Car("Toyota", "Camry", 2020)
print(car1.get_make())  # Виводить 'Toyota'
print(car1.get_model())  # Виводить 'Camry'
print(car1.get_year())   # Виводить 2020

car1.set_year(2022)
print(car1.get_year())   # Виводить 2022



