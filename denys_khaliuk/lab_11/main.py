class House:
    def __init__(self):
        self.floors = None
        self.rooms = None
        self.garage = None

    def __str__(self):
        return f"Будинок з {self.floors} поверхами, {self.rooms} кімнатами і {'з гаражем' if self.garage else 'без гаража'}."

class HouseBuilder:
    def __init__(self):
        self.house = House()

    def set_floors(self, floors):
        self.house.floors = floors
        return self

    def set_rooms(self, rooms):
        self.house.rooms = rooms
        return self

    def set_garage(self, has_garage):
        self.house.garage = has_garage
        return self

    def build(self):
        return self.house

builder = HouseBuilder()
house = builder.set_floors(2).set_rooms(4).set_garage(True).build()
print(house)
