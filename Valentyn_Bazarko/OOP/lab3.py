from abc import ABC, abstractmethod

# Інтерфейс команди
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Конкретні команди
class ConcreteCommandA(Command):
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.action_a()

class ConcreteCommandB(Command):
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.action_b()

# Отримувач
class Receiver:
    def action_a(self):
        print("Receiver: Виконує дію A.")

    def action_b(self):
        print("Receiver: Виконує дію B.")

# Виконавець
class Invoker:
    _on_start = None
    _on_finish = None

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self):
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: Виконує важливу роботу...")

        if isinstance(self._on_finish, Command):
            self._on_finish.execute()

# Використання
if __name__ == "__main__":
    receiver = Receiver()
    command_a = ConcreteCommandA(receiver)
    command_b = ConcreteCommandB(receiver)

    invoker = Invoker()
    invoker.set_on_start(command_a)
    invoker.set_on_finish(command_b)

    invoker.do_something_important()
