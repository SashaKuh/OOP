# Підсистеми (Складні частини системи)
class Engine:
    def __init__(self):
        self.is_running = False

    def start(self):
        if not self.is_running:
            print("Двигун: Запуск двигуна...")
            self.is_running = True
        else:
            print("Двигун вже запущений!")

    def stop(self):
        if self.is_running:
            print("Двигун: Зупинка двигуна...")
            self.is_running = False
        else:
            print("Двигун вже зупинений!")


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
        if not self.engine.is_running:
            print("Фасад автомобіля: Запуск автомобіля...")
            self.engine.start()
            self.transmission.engage()
            self.dashboard.turn_on_lights()
            print("Фасад автомобіля: Автомобіль запущений!")
        else:
            print("Автомобіль вже запущений!")

    def stop_car(self):
        if self.engine.is_running:
            print("Фасад автомобіля: Зупинка автомобіля...")
            self.engine.stop()
            self.transmission.disengage()
            self.dashboard.turn_off_lights()
            print("Фасад автомобіля: Автомобіль зупинено!")
        else:
            print("Автомобіль вже зупинено!")


# Використання фасаду з вибором користувача
if __name__ == "__main__":
    car = CarFacade()

    while True:
        print("\nВиберіть дію:")
        print("1 - Запустити автомобіль")
        print("2 - Зупинити автомобіль")
        print("3 - Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            car.start_car()
        elif choice == "2":
            car.stop_car()
        elif choice == "3":
            print("Завершення програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")
