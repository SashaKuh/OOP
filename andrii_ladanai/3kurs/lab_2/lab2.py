# Підсистеми (Складні частини системи)
class Engine:
    def start(self):
        print("Двигун: Запуск двигуна...")

    def stop(self):
        print("Двигун: Зупинка двигуна...")


class Transmission:
    def engage(self):
        print("Трансмісія: Включення трансмісії...")

    def disengage(self):
        print("Трансмісія: Вимкнення трансмісії...")


class Dashboard:
    def turn_on_lights(self):
        print("Панель приладів: Увімкнення підсвітки панелі...")

    def turn_off_lights(self):
        print("Панель приладів: Вимкнення підсвітки панелі...")

# Фасад (Facade)
class CarFacade:
    def __init__(self):
        self.engine = Engine()
        self.transmission = Transmission()
        self.dashboard = Dashboard()

    def start_car(self):
        print("Фасад автомобіля: Запуск автомобіля...")
        self.engine.start()
        self.transmission.engage()
        self.dashboard.turn_on_lights()
        print("Фасад автомобіля: Автомобіль запущений!")

    def stop_car(self):
        print("Фасад автомобіля: Зупинка автомобіля...")
        self.engine.stop()
        self.transmission.disengage()
        self.dashboard.turn_off_lights()
        print("Фасад автомобіля: Автомобіль зупинено!")

# Використання фасаду
if __name__ == "__main__":
    car = CarFacade()
    car.start_car()
    print()
    car.stop_car()
