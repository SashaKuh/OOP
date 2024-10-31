from abc import ABC, abstractmethod

# Абстрактний клас Компонент
class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

# Конкретний компонент
class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent"

# Абстрактний декоратор
class Decorator(Component):
    _component: Component

    def __init__(self, component: Component) -> None:
        self._component = component

    @abstractmethod
    def operation(self):
        pass

# Конкретні декоратори
class ConcreteDecoratorA(Decorator):
    def operation(self):
        return f"ConcreteDecoratorA({self._component.operation()})"

class ConcreteDecoratorB(Decorator):
    def operation(self):
        return f"ConcreteDecoratorB({self._component.operation()})"

# Використання
def client_code(component: Component):
    print(f"Результат: {component.operation()}")

if __name__ == "__main__":
    simple = ConcreteComponent()
    print("Client: У мене є простий компонент:")
    client_code(simple)
    print("\n")

    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Client: Тепер у мене є декорований компонент:")
    client_code(decorator2)
