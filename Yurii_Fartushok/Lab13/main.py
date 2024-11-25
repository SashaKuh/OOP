class CarCheck:
    def __init__(self, next_check=None):
        # Зберігаєм посилання на наступну перевірку в ланцюгу, якщо немає наступної тоді = None
        self.next_check = next_check

    def check(self, car):
        # чи є наступна перевірка в ланцюгу
        if self.next_check:
            # Передаємо перевірку до наступної перевірки в ланцюгу
            return self.next_check.check(car)
        return True


class EngineCheck(CarCheck):
    def check(self, car):
        if car['engine'] == 'working':
            print("Двигун в порядку.")
            return super().check(car)
        print("Двигун не працює.")
        return False


class TireCheck(CarCheck):
    def check(self, car):
        if car['tires'] == 'good':
            print("Шини в хорошому стані.")
            return super().check(car)
        print("Шини погані.")
        return False


class OilCheck(CarCheck):
    def check(self, car):
        if car['oil'] == 'full':
            print("Масло в нормі.")
            return super().check(car)
        print("Масло не в нормі.")
        return False


class LightsCheck(CarCheck):
    def check(self, car):
        if car['lights'] == 'working':
            print("Ліхтарі працюють.")
            return super().check(car)
        print("Ліхтарі не працюють.")
        return False


# Створюєм ланцюг перевірок
car_checks = EngineCheck(
    TireCheck(
        OilCheck(
            LightsCheck()
        )
    )
)

# Дані про автомобіль
car = {
    'engine': 'working',
    'tires': 'good',
    'oil': 'full',
    'lights': 'working'
}

# Результат
if car_checks.check(car):
    print("Так, автомобіль готовий до поїздки.")
else:
    print("Ні, автомобіль не готовий до поїздки.")
