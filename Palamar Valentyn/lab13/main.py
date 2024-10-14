class Visitor:
    def visit(self, element):
        pass


#відвідувач
class ConcreteVisitor(Visitor):
    def visit(self, element):
        if isinstance(element, ElementA):
            print("Відвідувач обробляє ElementA")
            element.operation_a()
        elif isinstance(element, ElementB):
            print("Відвідувач обробляє ElementB")
            element.operation_b()


# Інтерфейс елем
class Element:
    def accept(self, visitor):
        pass


#елементи
class ElementA(Element):
    def accept(self, visitor):
        visitor.visit(self)

    def operation_a(self):
        print("ElementA: виконується операція A")


class ElementB(Element):
    def accept(self, visitor):
        visitor.visit(self)

    def operation_b(self):
        print("ElementB: виконується операція B")


# Використання
if __name__ == "__main__":
    # Створення об'єктів елем
    elements = [ElementA(), ElementB()]

    # Створення відвідувача
    visitor = ConcreteVisitor()

    # Обробка елементів за допомогою відвідувача
    for element in elements:
        element.accept(visitor)
