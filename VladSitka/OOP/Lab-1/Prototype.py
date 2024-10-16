import copy


class Prototype:
    def clone(self):
        return copy.deepcopy(self)


class ConcretePrototype1(Prototype):
    def __init__(self, field1):
        self.field1 = field1

    def __str__(self):
        return f"Конкретний прототип 1 з полем 1: {self.field1}"


class ConcretePrototype2(Prototype):
    def __init__(self, field2):
        self.field2 = field2

    def __str__(self):
        return f"Конкретний прототип 2 з полем 2: {self.field2}"


if __name__ == "__main__":
    
    prototype1 = ConcretePrototype1("Значення 1")
    clone1 = prototype1.clone()

    
    prototype2 = ConcretePrototype2(123)
    clone2 = prototype2.clone()

    
    print(prototype1)
    print(clone1)

    print(prototype2)
    print(clone2)
