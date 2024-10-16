class Car:
    # Змінна класу для лічильника об'єктів
    object_counter = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        # Створення атрибуту, який залежить від інших атрибутів
        self.description = f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"
        # Збільшуємо лічильник об'єктів при кожному створенні об'єкту
        Car.object_counter += 1

    def generate_description(self):
        # Генеруємо опис об'єкта на основі його властивостей
        return self.description

# Створюємо декілька об'єктів на основі класу
car1 = Car("Toyota", "Corolla", 2017)
car2 = Car("Tesla", "Model S", 2022)

# Викликаємо метод для генерації опису об'єкта
print(car1.generate_description())
print(car2.generate_description())

# Виводимо кількість створених об'єктів
print("Number of objects created:", Car.object_counter)
