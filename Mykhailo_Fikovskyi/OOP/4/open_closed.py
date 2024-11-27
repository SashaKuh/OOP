class Product:
    def __init__(self, price):
        self.price = price

    def calculate_tax(self):
        return 0  

class Food(Product):
    def calculate_tax(self):
        return self.price * 0.05  

class Electronics(Product):
    def calculate_tax(self):
        return self.price * 0.15 

food = Food(100)  
electronics = Electronics(200) 

print(f"Food tax: {food.calculate_tax()}")
print(f"Electronics tax: {electronics.calculate_tax()}")
