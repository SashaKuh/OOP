class Observer:
    def update(self, temperature: float):
        pass

# Суб'єкт
class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = 0.0

    def register_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def set_temperature(self, temperature: float):
        self._temperature = temperature
        self.notify_observers()

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

# Конкретні спостерігачі
class TemperatureDisplay(Observer):
    def update(self, temperature: float):
        print(f"Температура на дисплеї: {temperature}°C")

class TemperatureAlert(Observer):
    def update(self, temperature: float):
        if temperature > 30:
            print("Попередження! Температура перевищує 30°C!")

# Використання
if __name__ == "__main__":
    # Створюємо суб'єкт
    weather_station = WeatherStation()

    # Створюємо спостерігачів
    temp_display = TemperatureDisplay()
    temp_alert = TemperatureAlert()

    # Реєструємо спостерігачів
    weather_station.register_observer(temp_display)
    weather_station.register_observer(temp_alert)

    # Змінюємо температуру
    weather_station.set_temperature(25)
    weather_station.set_temperature(35)
