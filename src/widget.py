from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """
    Маскирует строку с банковской картой или номером счета.

    Поддерживает форматы:
    - "Visa Platinum 7000..."
    - "Maestro 7000..."
    - "Счет 7365..."
    """

    if not isinstance(data, str):
        return "Некорректный формат входных данных"

    parts = data.strip().rsplit(" ", 1)

    if len(parts) != 2:
        return "Некорректный формат входных данных"

    name, number = parts

    name_clean = name.strip().lower()

    if name_clean in ("счет", "счёт"):
        return f"{name} {get_mask_account(number)}"

    return f"{name} {get_mask_card_number(number)}"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата ISO (YYYY-MM-DD...) в DD.MM.YYYY.
    """

    if not isinstance(date_str, str) or len(date_str) < 10:
        return "Некорректная дата"

    try:
        year, month, day = date_str[:10].split("-")
        return f"{day}.{month}.{year}"
    except ValueError:
        return "Некорректная дата"