
class PaymentStrategy:
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплата карткою: {amount} грн")


class CashPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплата готівкою: {amount} грн")


class ShoppingCart:
    def __init__(self):
        self.items = []
        self.payment_strategy = None

    def add_item(self, item):
        self.items.append(item)

    def set_payment_strategy(self, strategy):
        self.payment_strategy = strategy

    def checkout(self):
        total = sum(self.items)
        if self.payment_strategy:
            self.payment_strategy.pay(total)
        else:
            print("Оберіть спосіб оплати.")

# Використання
cart = ShoppingCart()
cart.add_item(100)
cart.add_item(200)

# Оплата карткою
cart.set_payment_strategy(CreditCardPayment())
cart.checkout()

# Оплата готівкою
cart.set_payment_strategy(CashPayment())
cart.checkout()
