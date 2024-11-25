# Приклад "брудного" коду
class MessyCalculator:
    def calculate_discount(self, price, customer_type, years_with_us):
        # Вся логіка змішана в одному методі
        discount = 0
        
        # Розрахунок знижки на основі типу клієнта
        if customer_type == "vip":
            discount = price * 0.2
        elif customer_type == "regular":
            discount = price * 0.1
            
        # Додаткова знижка за роки
        if years_with_us > 5:
            discount += price * 0.05
        elif years_with_us > 2:
            discount += price * 0.02
            
        # Перевірка максимальної знижки
        if discount > price * 0.3:
            discount = price * 0.3
            
        final_price = price - discount
        
        # Форматування та виведення результату змішане з логікою
        result = f"Original price: ${price:.2f}\n"
        result += f"Discount: ${discount:.2f}\n"
        result += f"Final price: ${final_price:.2f}"
        return result


# Код після рефакторингу
class CustomerDiscount:
    def calculate(self, customer_type: str, price: float) -> float:
        discounts = {
            "vip": 0.2,
            "regular": 0.1
        }
        return price * discounts.get(customer_type, 0)

class LoyaltyDiscount:
    def calculate(self, years: int, price: float) -> float:
        if years > 5:
            return price * 0.05
        elif years > 2:
            return price * 0.02
        return 0

class PriceCalculator:
    def __init__(self):
        self.customer_discount = CustomerDiscount()
        self.loyalty_discount = LoyaltyDiscount()
        
    def calculate_final_price(self, price: float, customer_type: str, years: int) -> tuple:
        # Розрахунок знижок
        base_discount = self.customer_discount.calculate(customer_type, price)
        loyalty_discount = self.loyalty_discount.calculate(years, price)
        
        # Загальна знижка не більше 30%
        total_discount = min(base_discount + loyalty_discount, price * 0.3)
        final_price = price - total_discount
        
        return final_price, total_discount

class PriceFormatter:
    @staticmethod
    def format_price_info(price: float, discount: float) -> str:
        final_price = price - discount
        return (
            f"Original price: ${price:.2f}\n"
            f"Discount: ${discount:.2f}\n"
            f"Final price: ${final_price:.2f}"
        )


# Приклад використання
if __name__ == "__main__":
    # Тест брудного коду
    print("=== Брудний код ===")
    messy = MessyCalculator()
    print(messy.calculate_discount(100, "vip", 6))
    
    print("\n=== Чистий код ===")
    calculator = PriceCalculator()
    formatter = PriceFormatter()
    
    price = 100
    final_price, discount = calculator.calculate_final_price(price, "vip", 6)
    print(formatter.format_price_info(price, discount))