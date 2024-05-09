# Базовий клас "Транспортний засіб"
class Transport:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed
    
    def move(self):
        print(f"{self.brand} рухається")

# Підклас "Грузовик", який успадковує властивості та методи від базового класу "Транспортний засіб"
class Truck(Transport):
    def __init__(self, brand, max_speed, max_load):
        self.brand = brand
        self.max_speed = max_speed
        self.max_load = max_load
    
    def load(self):
        print(f"{self.brand} завантажений")

# Створення об'єкту класу "Грузовик"
my_truck = Truck("MAN", 120, 5000)

# Виклик методів класу "Грузовик"
print(f"Максимальна швидкість грузовика {my_truck.brand}: {my_truck.max_speed} км/год")
my_truck.move()
my_truck.load()
