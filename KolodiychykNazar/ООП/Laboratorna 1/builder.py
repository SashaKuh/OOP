from abc import ABC, abstractmethod

class Product:
    def __init__(self):
        self.ingredients = []

    def __str__(self):
        return f"Pizza with ingredients: {', '.join(self.ingredients)}"

class Builder(ABC):
    
    @abstractmethod
    def add_cheese(self):
        pass

    @abstractmethod
    def add_pepperoni(self):
        pass

    @abstractmethod
    def add_mushrooms(self):
        pass

    @abstractmethod
    def build(self) -> Product:
        pass

class ConcreteBuilder(Builder):
    def __init__(self):
        self.pizza = Product()

    def add_cheese(self):
        self.pizza.ingredients.append("cheese")

    def add_pepperoni(self):
        self.pizza.ingredients.append("pepperoni")

    def add_mushrooms(self):
        self.pizza.ingredients.append("mushrooms")

    def build(self) -> Product:
        return self.pizza

class Director:
    def __init__(self, builder: Builder):
        self.builder = builder

    def make_pepperoni_pizza(self):
        self.builder.add_cheese()
        self.builder.add_pepperoni()
        return self.builder.build()

    def make_vegetarian_pizza(self):
        self.builder.add_cheese()
        self.builder.add_mushrooms()
        return self.builder.build()

if __name__ == "__main__":
    builder = ConcreteBuilder()
    director = Director(builder)

    pepperoni_pizza = director.make_pepperoni_pizza()
    print(pepperoni_pizza)  

    vegetarian_pizza = director.make_vegetarian_pizza()
    print(vegetarian_pizza)  
