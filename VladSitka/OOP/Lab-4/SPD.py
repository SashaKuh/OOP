class Order:
    def __init__(self, items, quantity):
        self.items = items
        self.quantity = quantity

    def calculate_total(self):
        return sum([item['price'] * self.quantity[i] for i, item in enumerate(self.items)])

class OrderPersistence:
    
    def save_to_file(order, filename):
        with open(filename, 'w') as file:
            file.write(f"Items: {order.items}\nQuantity: {order.quantity}\nTotal: {order.calculate_total()}")
