class Coffee:
    """Базовий клас, що представляє каву."""

    def cost(self):
        return 5  # Вартість базового продукту

    def ingredients(self):
        return "Coffee"  # Основний інгредієнт


class MilkDecorator:
    """Декоратор для додавання молока до кави."""

    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1  # Додає вартість молока

    def ingredients(self):
        return self._coffee.ingredients() + ", Milk"  # Додає молоко до інгредієнтів


class SugarDecorator:
    """Декоратор для додавання цукру до кави."""

    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 0.5  # Додає вартість цукру

    def ingredients(self):
        return self._coffee.ingredients() + ", Sugar"  # Додає цукор до інгредієнтів


# Демонстрація використання патерну
basic_coffee = Coffee()
print(f"Basic coffee cost: ${basic_coffee.cost()}")
print(f"Ingredients: {basic_coffee.ingredients()}")

# Додавання молока
milk_coffee = MilkDecorator(basic_coffee)
print(f"Milk coffee cost: ${milk_coffee.cost()}")
print(f"Ingredients: {milk_coffee.ingredients()}")

# Додавання цукру
sugar_milk_coffee = SugarDecorator(milk_coffee)
print(f"Sugar milk coffee cost: ${sugar_milk_coffee.cost()}")
print(f"Ingredients: {sugar_milk_coffee.ingredients()}")
