class Car:
    def __init__(self, speed, tank):
        self.speed = int(speed)
        self.tank = int(tank)
    def what_speed(self):
        if self.speed > 100:
            return "Швидко"
        else:
            return "Повільно"
    def amount_of_fuel(self):
        if self.tank >= 50:
            return "Повний бак"
        else:
            return "Пустий бак"
my_car = Car(100, 40)
print(my_car.what_speed())
print(my_car.amount_of_fuel())
print("________________________________________")

class Autobas(Car):
    def __init__(self, people, speed):
        self.people = int(people)
        self.speed = int(speed)
    def count_people(self):
        if self.people == 25:
            return "половина автобуса"
        elif self.people < 25:
            return "неповний автобус"
        else:
            return "повний автобус"
        
    def what_speed(self):
        if  self.speed > 60:
            return "Швидко"
        else:
            return "Повільно"
my_Autobas = Autobas(40, 80)
print(my_Autobas.count_people())
print(my_Autobas.what_speed())
