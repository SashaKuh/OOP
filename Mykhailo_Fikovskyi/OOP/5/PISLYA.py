def calculate_tax(amount, rate):
    return amount * rate  
amount_usa = 100
tax_usa = calculate_tax(amount_usa, 0.1) 
print(f"Податок для США: {tax_usa}")

amount_uk = 100
tax_uk = calculate_tax(amount_uk, 0.2)  
print(f"Податок для Великобританії: {tax_uk}")
