from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(data: str) -> str:
    """Маскирует карту или счет."""

    parts = data.split()
    name = parts[0]
    number = parts[1]

    if name == "Счет":
        return f"{name} {get_mask_account(number)}"
    else:
        return f"{name} {get_mask_card_number(number)}"


def get_date(date_str: str) -> str:
    """Форматирует дату."""
    return ".".join(date_str[:10].split("-")[::-1])



