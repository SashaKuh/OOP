class Customer:
    def __init__(self, name, loyalty_points):
        self.name = name
        self.loyalty_points = loyalty_points

class Order:
    def __init__(self, customer, total_amount):
        self.customer = customer
        self.total_amount = total_amount

    def calculate_discount(self):
        """Метод розрахунку знижки залежить від балів клієнта"""
        if self.customer.loyalty_points > 100:
            return self.total_amount * 0.1  # 10% знижка
        return 0

# Приклад використання
customer = Customer("Іван", 120)
order = Order(customer, 500)
print(f"Знижка: {order.calculate_discount()} грн")  
