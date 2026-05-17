import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("1234 5678 1234 5678", "1234 56** **** 5678"),
        (
            "1234",
            "Номер карты должен содержать 16 цифр. Попробуйте ещё раз.",
        ),
        (
            "abcd",
            "Формат номера карты неверный, он должен состоять только из цифр.",
        ),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("12345678901234567890", "**7890"),
        (
            "12345",
            "Номер счета должен содержать 20 цифр. Попробуйте ещё раз.",
        ),
        (
            "abcde",
            "Формат номера счета неверный, он должен состоять только из цифр.",
        ),
    ],
)
def test_get_mask_account(account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == expected