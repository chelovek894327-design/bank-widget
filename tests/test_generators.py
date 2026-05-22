import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


@pytest.fixture
def transactions() -> list[dict]:
    return [
        {
            "id": 1,
            "operationAmount": {
                "currency": {
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
        },
        {
            "id": 2,
            "operationAmount": {
                "currency": {
                    "code": "RUB"
                }
            },
            "description": "Оплата услуг",
        },
        {
            "id": 3,
            "operationAmount": {
                "currency": {
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
        },
    ]


@pytest.mark.parametrize(
    "currency, expected_ids",
    [
        ("USD", [1, 3]),
        ("RUB", [2]),
        ("EUR", []),
    ],
)
def test_filter_by_currency(
    transactions: list[dict],
    currency: str,
    expected_ids: list[int],
) -> None:
    result = list(filter_by_currency(transactions, currency))

    assert [transaction["id"] for transaction in result] == expected_ids


def test_filter_by_currency_empty_list() -> None:
    result = list(filter_by_currency([], "USD"))

    assert result == []


def test_transaction_descriptions(
    transactions: list[dict],
) -> None:
    result = list(transaction_descriptions(transactions))

    assert result == [
        "Перевод организации",
        "Оплата услуг",
        "Перевод со счета на счет",
    ]


def test_transaction_descriptions_empty() -> None:
    result = list(transaction_descriptions([]))

    assert result == []


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (
            1,
            3,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
            ],
        ),
        (
            9998,
            10000,
            [
                "0000 0000 0000 9998",
                "0000 0000 0000 9999",
                "0000 0000 0001 0000",
            ],
        ),
    ],
)
def test_card_number_generator(
    start: int,
    stop: int,
    expected: list[str],
) -> None:
    result = list(card_number_generator(start, stop))

    assert result == expected


def test_card_number_generator_single() -> None:
    result = list(card_number_generator(1, 1))

    assert result == [
        "0000 0000 0000 0001"
    ]


def test_card_number_generator_empty() -> None:
    result = list(card_number_generator(5, 1))

    assert result == []
