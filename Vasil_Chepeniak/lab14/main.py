class Order:
    def __init__(self, product_name: str, price: float):
        self.product_name = product_name
        self.price = price

class PriceCalculator:
    def calculate_with_tax(self, order: Order) -> float:
        tax = 0.2  # 20% податок
        return order.price + (order.price * tax)

class OrderPrinter:
    def print_order(self, order: Order) -> str:
        return f"Товар: {order.product_name}, Ціна: {order.price} грн"

# Приклад використання
def main():
    # Створюємо замовлення
    order = Order("Телефон", 1000)
    
    # Рахуємо ціну з податком
    calculator = PriceCalculator()
    final_price = calculator.calculate_with_tax(order)
    
    # Друкуємо інформацію
    printer = OrderPrinter()
    order_info = printer.print_order(order)
    
    print(order_info)
    print(f"Ціна з податком: {final_price} грн")

if __name__ == "__main__":
    main()