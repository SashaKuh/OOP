class Product:
    def operation(self):
        pass

class ConcreteProductA(Product):
    def operation(self):
        return "Продукт A"

class ConcreteProductB(Product):
    def operation(self):
        return "Продукт B"

class Creator:
    def factory_method(self, product_type):
        if product_type == 'A':
            return ConcreteProductA()
        elif product_type == 'B':
            return ConcreteProductB()
        else:
            return None

creator = Creator()

product_a = creator.factory_method('A')
print(product_a.operation())

product_b = creator.factory_method('B')
print(product_b.operation())