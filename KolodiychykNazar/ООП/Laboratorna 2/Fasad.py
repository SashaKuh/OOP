
class PaymentProcessor:
    def process_payment(self, amount):
        print(f"Processing payment of {amount}.")

class Inventory:
    def check_availability(self, item):
        print(f"Checking availability for {item}.")
        return True  
class Shipping:
    def ship_item(self, item):
        print(f"Shipping {item}.")

class OrderFacade:
    def __init__(self):
        self.payment_processor = PaymentProcessor()
        self.inventory = Inventory()
        self.shipping = Shipping()

    def place_order(self, item, amount):
        if self.inventory.check_availability(item):
            self.payment_processor.process_payment(amount)
            self.shipping.ship_item(item)
            print("Order placed successfully!")
        else:
            print("Item is not available.")


if __name__ == "__main__":
    order_facade = OrderFacade()
    order_facade.place_order("Laptop", 1200)
