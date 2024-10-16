class Coffee:
    def cost(self):
        return 5

class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 2

class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1

basic_coffee = Coffee()
print(f"Вартість базової кави: {basic_coffee.cost()}")  

milk_coffee = MilkDecorator(basic_coffee)
print(f"Вартість кави з молоком: {milk_coffee.cost()}")  

sugar_milk_coffee = SugarDecorator(milk_coffee)
print(f"Вартість кави з молоком і цукром: {sugar_milk_coffee.cost()}")  
