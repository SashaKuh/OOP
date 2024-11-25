from abc import ABC, abstractmethod

# Receiver (Отримувач) - клас, який виконує фактичну роботу
class SmartDevice:
    """
    Клас, що представляє розумний пристрій з можливістю керування станом та температурою.
    Виступає у ролі Receiver у патерні Command.
    """
    def __init__(self, name):
        self.name = name
        self.is_on = False  # Початковий стан - вимкнено
        self.temperature = 20  # Початкова температура

    def turn_on(self):
        """Вмикає пристрій"""
        self.is_on = True
        return f"{self.name} увімкнено"

    def turn_off(self):
        """Вимикає пристрій"""
        self.is_on = False
        return f"{self.name} вимкнено"

    def set_temperature(self, temperature):
        """Встановлює температуру пристрою"""
        self.temperature = temperature
        return f"Встановлено температуру {self.temperature}°C для {self.name}"

    def get_status(self):
        """Повертає поточний стан пристрою"""
        status = "увімкнено" if self.is_on else "вимкнено"
        return f"{self.name} - {status}, температура: {self.temperature}°C"

# Command (Команда) - абстрактний базовий клас для всіх команд
class Command(ABC):
    """
    Абстрактний клас команди, що визначає інтерфейс для всіх конкретних команд.
    Кожна команда повинна мати можливість виконання та скасування.
    """
    @abstractmethod
    def execute(self):
        """Виконує команду"""
        pass

    @abstractmethod
    def undo(self):
        """Скасовує виконання команди"""
        pass

# Конкретні реалізації команд
class TurnOnCommand(Command):
    """Команда для вмикання пристрою"""
    def __init__(self, device):
        self.device = device

    def execute(self):
        return self.device.turn_on()

    def undo(self):
        return self.device.turn_off()

class TurnOffCommand(Command):
    """Команда для вимикання пристрою"""
    def __init__(self, device):
        self.device = device

    def execute(self):
        return self.device.turn_off()

    def undo(self):
        return self.device.turn_on()

class SetTemperatureCommand(Command):
    """Команда для встановлення температури"""
    def __init__(self, device, temperature):
        self.device = device
        self.temperature = temperature
        self.previous_temperature = device.temperature  # Зберігаємо попередню температуру для можливості скасування

    def execute(self):
        self.previous_temperature = self.device.temperature
        return self.device.set_temperature(self.temperature)

    def undo(self):
        return self.device.set_temperature(self.previous_temperature)

# Invoker (Викликач) - клас, що керує виконанням команд
class SmartHomeController:
    """
    Контролер розумного будинку, який виконує команди та зберігає їх історію.
    Виступає у ролі Invoker у патерні Command.
    """
    def __init__(self):
        self.command_history = []  # Історія виконаних команд для можливості скасування

    def execute_command(self, command):
        """Виконує команду та додає її в історію"""
        result = command.execute()
        self.command_history.append(command)
        return result

    def undo_last_command(self):
        """Скасовує останню виконану команду"""
        if self.command_history:
            command = self.command_history.pop()
            return command.undo()
        return "Немає команд для скасування"

def print_menu():
    """Виводить меню опцій для користувача"""
    print("\nМеню керування розумним будинком:")
    print("1. Увімкнути пристрій")
    print("2. Вимкнути пристрій")
    print("3. Встановити температуру")
    print("4. Скасувати останню команду")
    print("5. Показати статус пристроїв")
    print("0. Вийти")

def main():
    """
    Головна функція програми.
    Створює пристрої, обробляє команди користувача та керує їх виконанням.
    """
    # Створюємо словник доступних пристроїв
    devices = {
        1: SmartDevice("Світло у вітальні"),
        2: SmartDevice("Термостат у спальні"),
        3: SmartDevice("Світло у кухні")
    }
    
    controller = SmartHomeController()

    # Головний цикл програми
    while True:
        print_menu()
        choice = input("Виберіть опцію: ")

        if choice == "0":
            print("До побачення!")
            break

        elif choice in ["1", "2"]:  # Обробка команд вмикання/вимикання
            print("\nДоступні пристрої:")
            for id, device in devices.items():
                print(f"{id}. {device.name}")
            
            try:
                device_id = int(input("Виберіть номер пристрою: "))
                if device_id not in devices:
                    print("Неправильний номер пристрою!")
                    continue
                
                device = devices[device_id]
                # Створюємо відповідну команду залежно від вибору
                command = TurnOnCommand(device) if choice == "1" else TurnOffCommand(device)
                print(controller.execute_command(command))
            
            except ValueError:
                print("Будь ласка, введіть число!")

        elif choice == "3":  # Обробка команди встановлення температури
            print("\nДоступні пристрої:")
            for id, device in devices.items():
                print(f"{id}. {device.name}")
            
            try:
                device_id = int(input("Виберіть номер пристрою: "))
                if device_id not in devices:
                    print("Неправильний номер пристрою!")
                    continue
                
                temperature = float(input("Введіть температуру: "))
                device = devices[device_id]
                command = SetTemperatureCommand(device, temperature)
                print(controller.execute_command(command))
            
            except ValueError:
                print("Будь ласка, введіть коректне число!")

        elif choice == "4":  # Скасування останньої команди
            print(controller.undo_last_command())

        elif choice == "5":  # Показ статусу всіх пристроїв
            print("\nСтатус пристроїв:")
            for device in devices.values():
                print(device.get_status())

        else:
            print("Неправильний вибір! Спробуйте ще раз.")

if __name__ == "__main__":
    main()