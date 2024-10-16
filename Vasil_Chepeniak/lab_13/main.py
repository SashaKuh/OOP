class Light:
    def turn_on(self):
        print("The light is on")
    
    def turn_off(self):
        print("The light is off")

class Command:
    def execute(self):
        pass

class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light
    
    def execute(self):
        self.light.turn_on()

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light
    
    def execute(self):
        self.light.turn_off()

class RemoteControl:
    def __init__(self):
        self.command = None
    
    def set_command(self, command: Command):
        self.command = command
    
    def press_button(self):
        if self.command:
            self.command.execute()

if __name__ == "__main__":

    light = Light()
    
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)
    
    remote = RemoteControl()
    
    remote.set_command(light_on)
    remote.press_button()  # The light is on
    
    remote.set_command(light_off)
    remote.press_button()  # The light is off
