from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    assert get_mask_card_number("1234567812345678") == "1234 56** **** 5678"
    assert get_mask_card_number("1234 5678 1234 5678") == "1234 56** **** 5678"
    assert (
        get_mask_card_number("1234")
        == "Номер карты должен содержать 16 цифр. Попробуйте ещё раз."
    )
    assert (
        get_mask_card_number("abcd")
        == "Формат номера карты неверный, он должен состоять только из цифр."
    )


def test_get_mask_account() -> None:
    assert get_mask_account("12345678901234567890") == "**7890"
    assert (
        get_mask_account("12345")
        == "Номер счета должен содержать 20 цифр. Попробуйте ещё раз."
    )
    assert (
        get_mask_account("abcde")
        == "Формат номера счета неверный, он должен состоять только из цифр."
    )
