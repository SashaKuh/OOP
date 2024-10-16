#Створення класу з атрибутами
class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.full_description = f"{year} {brand} {model}, Ціна: {price} грн"
my_car = Car("Toyota", "Camry", 2020, 25000)
print(my_car.full_description)  

#Метод що генерує опис об'экта
class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def generate_description(self):
        return f"{self.year} {self.brand} {self.model}, Ціна: {self.price} грн"

my_car = Car("Toyota", "Camry", 2020, 25000)
print(my_car.generate_description())  

#Створення об'єктів та виклик методу 
car1 = Car("BMW", "X5", 2018, 35000)
car2 = Car("Mercedes-Benz", "E-Class", 2019, 30000)

print(car1.generate_description())  
print(car2.generate_description())  

#Поняття змінної класу
class Car:
    total_cars = 0

    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        Car.total_cars += 1

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars

car1 = Car("BMW", "X5", 2018, 35000)
car2 = Car("Mercedes-Benz", "E-Class", 2019, 30000)
print("Кількість автомобілів:", Car.get_total_cars())  

