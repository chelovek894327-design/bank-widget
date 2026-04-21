
def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты."""
    new_card_number = card_number.replace(" ", "")

    if not new_card_number.isdigit():
        return "Формат номера карты неверный, он должен состоять только из цифр."

    if len(new_card_number) != 16:
        return "Номер карты должен содержать 16 цифр. Попробуйте ещё раз."

    return f"{new_card_number[:4]} {new_card_number[4:6]}** **** {new_card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счета."""
    new_account_number = account_number.replace(" ", "")

    if not new_account_number.isdigit():
        return "Формат номера счета неверный, он должен состоять только из цифр."

    if len(new_account_number) != 20:
        return "Номер счета должен содержать 20 цифр. Попробуйте ещё раз."

    return f"**{new_account_number[-4:]}"
