def get_mask_card_number(card: str):
    """Функция, маскирующая введенный номер карты"""
    mask = card.replace(x[6:-4], "******")
    result = mask
    return result


x = "7000792289606361"
print(get_mask_card_number(x))


def get_mask_account(account: str):
    """Функция, маскирующая номер счета"""
    mask_2 = y.replace(y[0:-4], "**")
    return mask_2


y = "73654108430135874305"
print(get_mask_account(y))
