from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class StartEngineCommand(Command):
    def __init__(self, car):
        self.car = car

    def execute(self):
        self.car.start_engine()


class StopEngineCommand(Command):
    def __init__(self, car):
        self.car = car

    def execute(self):
        self.car.stop_engine()


class ShiftGearCommand(Command):
    def __init__(self, car, gear):
        self.car = car
        self.gear = gear

    def execute(self):
        self.car.shift_gear(self.gear)


class Car:
    def __init__(self):
        self.engine_on = False
        self.gear = "P"

    def start_engine(self):
        if not self.engine_on:
            self.engine_on = True
            print("The engine is started.")
        else:
            print("The engine is already running.")

    def stop_engine(self):
        if self.engine_on:
            self.engine_on = False
            print("The engine is stopped.")
        else:
            print("The engine is already off.")

    def shift_gear(self, gear):
        self.gear = gear
        print(f"Gear shifted to {self.gear}.")


class CarController:
    def execute_command(self, command):
        command.execute()


car_obj = Car()
controller = CarController()

controller.execute_command(StartEngineCommand(car_obj))
controller.execute_command(ShiftGearCommand(car_obj, "1"))
controller.execute_command(ShiftGearCommand(car_obj, "P"))
controller.execute_command(StopEngineCommand(car_obj))
