# Компонент
class Pizza:
    def cost(self):
        return 10

# Базовий декоратор
class PizzaDecorator(Pizza):
    def __init__(self, pizza):
        self._pizza = pizza

    def cost(self):
        return self._pizza.cost()

# Декоратор: додавання сиру
class CheeseDecorator(PizzaDecorator):
    def cost(self):
        return self._pizza.cost() + 5

# Декоратор: додавання бекону
class BaconDecorator(PizzaDecorator):
    def cost(self):
        return self._pizza.cost() + 7

# Використання
pizza = Pizza()
print("Базова піца:", pizza.cost())

pizza_with_cheese = CheeseDecorator(pizza)
print("Піца з сиром:", pizza_with_cheese.cost())

pizza_with_cheese_and_bacon = BaconDecorator(pizza_with_cheese)
print("Піца з сиром і беконом:", pizza_with_cheese_and_bacon.cost())
