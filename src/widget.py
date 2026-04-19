from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account: str) -> str:
    """Маскирует номер карты или счета в строке с типом продукта."""
    parts = card_or_account.split()
    number = parts[-1]
    name = " ".join(parts[:-1])

    if name.lower() == "счет":
        return f"{name} {get_mask_account(number)}"

    return f"{name} {get_mask_card_number(number)}"


def get_date(date_string: str) -> str:
    """Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ."""
    return f"{date_string[8:10]}.{date_string[5:7]}.{date_string[0:4]}"