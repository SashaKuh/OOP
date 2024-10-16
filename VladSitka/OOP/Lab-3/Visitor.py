
class Element:
    def accept(self, visitor):
        pass


class ConcreteElementA(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_a(self)

    def operation_a(self):
        return "Operation A"


class ConcreteElementB(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_b(self)

    def operation_b(self):
        return "Operation B"


class Visitor:
    def visit_concrete_element_a(self, element):
        pass

    def visit_concrete_element_b(self, element):
        pass


class ConcreteVisitor(Visitor):
    def visit_concrete_element_a(self, element):
        result = element.operation_a()
        print(f"Visitor: {result}")

    def visit_concrete_element_b(self, element):
        result = element.operation_b()
        print(f"Visitor: {result}")

if __name__ == "__main__":
    elements = [ConcreteElementA(), ConcreteElementB()]
    visitor = ConcreteVisitor()

    for element in elements:
        element.accept(visitor)
