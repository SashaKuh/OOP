def calculate_discount(price, discount_type):
    if discount_type == "percentage":
        discount = price * 0.1
        final_price = price - discount
        print(f"Знижка 10%. Остаточна ціна: {final_price}")
    elif discount_type == "fixed":
        discount = 20
        final_price = price - discount
        print(f"Фіксована знижка 20. Остаточна ціна: {final_price}")
    else:
        print("Тип знижки не підтримується.")
