class Car:
    def __init__(self):
        self.make = None
        self.model = None
        self.color = None
        self.engine_capacity = None

    def __str__(self):
        return (f"Car: make - {self.make}, model - {self.model}, "
                f"color - {self.color}, engine capacity - {self.engine_capacity} cm3.")


class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_make(self, make):
        self.car.make = make
        return self

    def set_model(self, model):
        self.car.model = model
        return self

    def set_color(self, color):
        self.car.color = color
        return self

    def set_engine_capacity(self, engine_capacity):
        self.car.engine_capacity = engine_capacity
        return self

    def get_car(self):
        return self.car


class CarDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_skoda_octavia(self):
        return (self.builder
                .set_make("Skoda")
                .set_model("Octavia")
                .set_color("White")
                .set_engine_capacity(1600))

    def construct_audi_a6(self):
        return (self.builder
                .set_make("Audi")
                .set_model("A6")
                .set_color("Black")
                .set_engine_capacity(3000))


builder = CarBuilder()
director = CarDirector(builder)

skoda_octavia = director.construct_skoda_octavia().get_car()
print(skoda_octavia)

audi_a6 = director.construct_audi_a6().get_car()
print(audi_a6)
