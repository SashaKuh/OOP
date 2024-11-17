class Customer:
    def __init__(self, name, loyalty_points):
        self.name = name
        self.loyalty_points = loyalty_points

    def calculate_discount(self, total_amount):
        """Метод розрахунку знижки тепер знаходиться в класі Customer"""
        if self.loyalty_points > 100:
            return total_amount * 0.1  # 10% знижка
        return 0

class Order:
    def __init__(self, customer, total_amount):
        self.customer = customer
        self.total_amount = total_amount

    def get_discount(self):
        """Викликаємо метод розрахунку знижки у клієнта"""
        return self.customer.calculate_discount(self.total_amount)

# Приклад використання після рефакторингу
customer = Customer("Іван", 120)
order = Order(customer, 500)
print(f"Знижка: {order.get_discount()} грн")  # Виведе: Знижка: 50.0 грн
