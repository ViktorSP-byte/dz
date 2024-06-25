def mask_account_card(card: str):
    """Функция, маскирующая номер карты и счета"""
    for member in card:
        if "V" in member:
            mask = card.replace(card[14:-4], "******")
            result = mask
            return result
        elif "M" in member:
            mask = card.replace(card[14:-4], "******")
            result = mask
            return result
        elif "С" in member:
            mask = card.replace(card[5:-4], "**")
            result = mask
            return result


card = "Maestro 1596837868705199"


print(mask_account_card(card))


def get_data(data):
    """Функция, меняющая формат даты"""
    result = data[8:10] + "." + data[5:7] + "." + data[:4]
    return result


data = "2018-07-11T02:26:18.671407"
print(get_data(data))
