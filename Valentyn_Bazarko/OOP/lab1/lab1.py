from abc import ABC, abstractmethod

# Абстрактний клас для продукту
class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

# Конкретні продукти
class ConcreteProductA(Product):
    def operation(self):
        return "Результат продукту A"

class ConcreteProductB(Product):
    def operation(self):
        return "Результат продукту B"

# Абстрактна фабрика
class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self):
        product = self.factory_method()
        result = f"Creator: працює з {product.operation()}"
        return result

# Конкретні фабрики
class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()

# Використання
def client_code(creator: Creator):
    print(f"Client: Я не знаю, який конкретний продукт буде створено, але фабрика вже створила: {creator.some_operation()}")

if __name__ == "__main__":
    print("App: Запущено з ConcreteCreatorA.")
    client_code(ConcreteCreatorA())
    print("\n")
    print("App: Запущено з ConcreteCreatorB.")
    client_code(ConcreteCreatorB())
