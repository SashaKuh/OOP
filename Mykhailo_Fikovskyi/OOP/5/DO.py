def calculate_tax_usa(amount):
    return amount * 0.1  

def calculate_tax_uk(amount):
    return amount * 0.2  

amount_usa = 100
tax_usa = calculate_tax_usa(amount_usa)
print(f"Податок для США: {tax_usa}")

amount_uk = 100
tax_uk = calculate_tax_uk(amount_uk)
print(f"Податок для Великобританії: {tax_uk}")
