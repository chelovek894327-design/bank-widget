from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(data: str) -> str:
    """
    Маскирует строку с банковской картой или номером счета.
    """
    parts = data.split(maxsplit=1)

    if len(parts) != 2:
        return "Некорректный формат входных данных"

    name, number = parts

    if name == "Счет":
        return f"{name} {get_mask_account(number)}"

    return f"{name} {get_mask_card_number(number)}"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата ISO в DD.MM.YYYY.
    """
    if len(date_str) < 10:
        return "Некорректная дата"

    year, month, day = date_str[:10].split("-")

    return f"{day}.{month}.{year}"

