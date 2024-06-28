def mask_account_card(card: str):
    """Функция, маскирующая номер карты и счета"""
    for _card in card:
        if "Счет" in card:
            mask_1 = card.replace(x[5:-4], "**")
            result = mask_1
            return result
        else:
            mask_2 = card.replace(x[14:-4], "******")
            result = mask_2
            return result


x = "Счет 64686473678894779589"
print(mask_account_card(x))
