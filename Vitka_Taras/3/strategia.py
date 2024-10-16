
class Strategy:
    def execute(self, data):
        pass


class ConcreteStrategyA(Strategy):
    def execute(self, data):
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def execute(self, data):
        return sorted(data, reverse=True)


class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute_strategy(self, data):
        return self._strategy.execute(data)

if __name__ == "__main__":
    data = [5, 2, 9, 1, 5, 6]

    context = Context(ConcreteStrategyA())
    print("Sorted (A):", context.execute_strategy(data))

    context.set_strategy(ConcreteStrategyB())
    print("Sorted (B):", context.execute_strategy(data))
