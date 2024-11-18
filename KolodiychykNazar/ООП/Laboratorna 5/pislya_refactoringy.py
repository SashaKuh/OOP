def calculate_price(price, tax, discount):
    tax_amount = price * (tax / 100)
    discount_amount = price * (discount / 100)
    total_price = price + tax_amount - discount_amount
    return total_price, tax_amount, discount_amount

def print_price_details(price, tax, discount):
    total_price, tax_amount, discount_amount = calculate_price(price, tax, discount)
    print("Tax:", tax_amount)
    print("Discount:", discount_amount)
    print("Total price:", total_price)

price = 100
tax = 10
discount = 20
print_price_details(price, tax, discount)
