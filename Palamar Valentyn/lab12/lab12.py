class Beverage:    
    def cost(self):
        return 0

class Coffee(Beverage):    
    def cost(self):
        return 5

class Tea(Beverage):    
    def cost(self):
        return 3

class BeverageDecorator(Beverage): #Декоратор
    def __init__(self, beverage):
        self.beverage = beverage

class MilkDecorator(BeverageDecorator): #Декоратор для додавання молока до напою    
    def cost(self):
        return self.beverage.cost() + 1  

class SugarDecorator(BeverageDecorator): #Декоратор для додавання цукру до напою    
    def cost(self):
        return self.beverage.cost() + 0.5

if __name__ == "__main__":
    beverage = Coffee()
    print(f"Вартість кави: {beverage.cost()} грн") #кава без домішок 

    beverage_with_milk = MilkDecorator(beverage)
    print(f"Вартість кави з молоком: {beverage_with_milk.cost()} грн")

    beverage_with_milk_and_sugar = SugarDecorator(beverage_with_milk)
    print(f"Вартість кави з молоком і цукром: {beverage_with_milk_and_sugar.cost()} грн")

    tea_with_sugar = SugarDecorator(Tea())
    print(f"Вартість чаю з цукром: {tea_with_sugar.cost()} грн")
