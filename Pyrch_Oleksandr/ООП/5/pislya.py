class Calculator:
    def add(self, a, b):
        return a + b

class Printer:
    @staticmethod
    def print_result(result):
        print(result)


calculator = Calculator()
printer = Printer()

result = calculator.add(3, 5)
printer.print_result(result)
