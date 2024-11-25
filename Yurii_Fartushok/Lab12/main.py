# Регулювання температури
class TemperatureControl:
    def set_temperature(self, plant_type):
        if plant_type == "apple":
            print("Температура налаштована на 22°C для яблук.")
        elif plant_type == "cactus":
            print("Температура налаштована на 30°C для кактусів.")
        else:
            print("Температура налаштована на стандартне значення.")


# Регулювання вологості
class HumidityControl:
    def set_humidity(self, plant_type):
        if plant_type == "apple":
            print("Вологість налаштована на 60% для яблук.")
        elif plant_type == "cactus":
            print("Вологість налаштована на 20% для кактусів.")
        else:
            print("Вологість налаштована на стандартне значення.")


# Регулювання світла
class LightingControl:
    def set_lighting(self, plant_type):
        if plant_type == "apple":
            print("Освітлення налаштовано на середнє для яблук.")
        elif plant_type == "cactus":
            print("Освітлення налаштовано на яскраве для кактусів.")
        else:
            print("Освітлення налаштовано на стандартне значення.")


# Фасад зі всіма налаштуваннями
class PlantCareFacade:
    def __init__(self):
        self.temperature_control = TemperatureControl()
        self.humidity_control = HumidityControl()
        self.lighting_control = LightingControl()

    def set_conditions(self, plant_type):
        print(f"Налаштовуємо умови для рослини: {plant_type}")
        self.temperature_control.set_temperature(plant_type)
        self.humidity_control.set_humidity(plant_type)
        self.lighting_control.set_lighting(plant_type)
        print("Умови налаштовано.\n")


plant_care = PlantCareFacade()

# Умови для яблука
plant_care.set_conditions("apple")

# Умови для кактуса
plant_care.set_conditions("cactus")

# Інші рослини
plant_care.set_conditions("other")
