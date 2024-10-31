class Command:
    """Інтерфейс команди."""
    def execute(self):
        pass


class Light:
    """Клас, що представляє світло."""

    def on(self):
        print("Світло увімкнено.")

    def off(self):
        print("Світло вимкнено.")


class LightOnCommand(Command):
    """Команда для увімкнення світла."""

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()


class LightOffCommand(Command):
    """Команда для вимкнення світла."""

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()


class RemoteControl:
    """Клас, що представляє пульт дистанційного керування."""

    def __init__(self):
        self.command = None

    def set_command(self, command):
        """Метод для налаштування команди."""
        self.command = command

    def press_button(self):
        """Метод для виконання команди."""
        if self.command:
            self.command.execute()


# Демонстрація використання патерну Команда
if __name__ == "__main__":
    light = Light()
    
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    remote = RemoteControl()

    # Увімкнути світло
    remote.set_command(light_on)
    remote.press_button()

    # Вимкнути світло
    remote.set_command(light_off)
    remote.press_button()
