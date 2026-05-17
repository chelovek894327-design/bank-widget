from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """
    Маскирует номер банковской карты или счета.

    Функция принимает строку с названием карты или счета
    и номером, затем возвращает строку с замаскированным номером.

    Args:
        data: Строка с названием и номером карты или счета.

    Returns:
        Строка с замаскированным номером карты или счета.
    """
    parts = data.split()

    if len(parts) < 2:
        return "Некорректный формат входных данных"

    number = parts[-1]
    name = " ".join(parts[:-1])

    if name == "Счет":
        return f"{name} {get_mask_account(number)}"

    return f"{name} {get_mask_card_number(number)}"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата ISO в формат DD.MM.YYYY.

    Args:
        date_str: Дата в формате YYYY-MM-DDTHH:MM:SS.

    Returns:
        Дата в формате DD.MM.YYYY.
    """
    if len(date_str) < 10:
        return "Некорректная дата"

    year, month, day = date_str[:10].split("-")

    return f"{day}.{month}.{year}"
