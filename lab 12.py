class House:
    def cost(self):
        return 100000  


class HouseDecorator(House):
    def __init__(self, house):
        self._house = house

    def cost(self):
        return self._house.cost()


class FurnitureDecorator(HouseDecorator):
    def cost(self):
        return self._house.cost() + 15000  

class LightingDecorator(HouseDecorator):
    def cost(self):
        return self._house.cost() + 5000  

# Використання
house = House()
print("Базовий будинок:", house.cost())

house_with_furniture = FurnitureDecorator(house)
print("Будинок з меблями:", house_with_furniture.cost())

house_with_furniture_and_lighting = LightingDecorator(house_with_furniture)
print("Будинок з меблями і освітленням:", house_with_furniture_and_lighting.cost())
