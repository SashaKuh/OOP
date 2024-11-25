def get_final_price(price, has_discount, is_vip):
    if has_discount and is_vip:
        return price * 0.8
    elif has_discount and not is_vip:
        return price * 0.9
    elif not has_discount and is_vip:
        return price * 0.85
    else:
        return price


price = 100
has_discount = False
is_vip = True

final_price = get_final_price(price, has_discount, is_vip)
print(f"Фінальна ціна: {final_price}")
