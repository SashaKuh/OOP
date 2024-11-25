def get_final_price(price, has_discount, is_vip):
    discount = calculate_discount(has_discount, is_vip)
    return price * (1 - discount)



def calculate_discount(has_discount, is_vip):
    if has_discount:
        return 0.1 + (0.1 if is_vip else 0)
    return 0.15 if is_vip else 0


# Виконання програми
price = 100
has_discount = False
is_vip = True

final_price = get_final_price(price, has_discount, is_vip)
print(f"Фінальна ціна: {final_price}")
