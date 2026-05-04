from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(data: str) -> str:
    if data.startswith("Счет"):
        return get_mask_account(data.split()[1])
    else:
        parts = data.split()
        return f"{parts[0]} {get_mask_card_number(parts[1])}"


def get_date(date_str: str) -> str:
    return ".".join(reversed(date_str[:10].split("-")))



