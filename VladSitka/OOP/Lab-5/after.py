def calculate_discount(price, discount_type):
    discount = _get_discount(price, discount_type)
    if discount is not None:
        final_price = price - discount
        print(f"Остаточна ціна: {final_price}")
    else:
        print("Тип знижки не підтримується.")

def _get_discount(price, discount_type):
    if discount_type == "percentage":
        return price * 0.1
    elif discount_type == "fixed":
        return 20
    return None
