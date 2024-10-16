from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

class ConcreteProductA(Product):
    def operation(self) -> str:
        return "Результат ConcreteProductA"


class ConcreteProductB(Product):
    def operation(self) -> str:
        return "Результат ConcreteProductB"


class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        return f"Creator: {product.operation()}"

class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()

def client_code(creator: Creator) -> None:
    print(creator.some_operation())

client_code(ConcreteCreatorA())
client_code(ConcreteCreatorB())
