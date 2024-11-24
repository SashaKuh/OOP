""" Приклад брудного коду
class Shop:
    def __init__(self):
        self.items = []
        self.money = 0
    
    def add_item(self, name, price):
        # Додаємо товар і робимо все в одному методі
        self.items.append({"name": name, "price": price})
        print(f"Додано товар: {name}")
        print(f"Ціна: {price}")
        print(f"Всього товарів: {len(self.items)}")
    
    def sell_item(self, name):
        # Продаємо товар і робимо все тут же
        for item in self.items:
            if item["name"] == name:
                self.money += item["price"]
                self.items.remove(item)
                print(f"Продано товар: {name}")
                print(f"Отримано грошей: {item['price']}")
                print(f"Всього грошей: {self.money}")
                return
        print("Товар не знайдено")

# Використання
shop = Shop()
shop.add_item("Телефон", 1000)
shop.add_item("Навушники", 200)
shop.sell_item("Телефон")
"""
# код після рефакторингу: 
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class Shop:
    def __init__(self):
        self.products = []
        self.money = 0
    
    def add_product(self, name: str, price: float):
        product = Product(name, price)
        self.products.append(product)
        return product
    
    def sell_product(self, name: str) -> bool:
        for product in self.products:
            if product.name == name:
                self.money += product.price
                self.products.remove(product)
                return True
        return False

class ShopPrinter:
    @staticmethod
    def print_add_result(product: Product):
        print(f"Додано товар: {product.name}")
        print(f"Ціна: {product.price}")
    
    @staticmethod
    def print_sell_result(success: bool, product_name: str, money: float):
        if success:
            print(f"Продано товар: {product_name}")
            print(f"Всього грошей: {money}")
        else:
            print("Товар не знайдено")

# Використання
shop = Shop()
printer = ShopPrinter()

# Додаємо товари
product = shop.add_product("Телефон", 1000)
printer.print_add_result(product)

product = shop.add_product("Навушники", 200)
printer.print_add_result(product)

# Продаємо товар
success = shop.sell_product("Телефон")
printer.print_sell_result(success, "Телефон", shop.money)