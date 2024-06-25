def mask_account_card(card: str):
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
