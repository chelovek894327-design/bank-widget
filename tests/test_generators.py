from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator,
)


def test_filter_by_currency() -> None:
    transactions = [
        {
            "id": 1,
            "operationAmount": {
                "currency": {"code": "USD"}
            },
        },
        {
            "id": 2,
            "operationAmount": {
                "currency": {"code": "RUB"}
            },
        },
        {
            "id": 3,
            "operationAmount": {
                "currency": {"code": "USD"}
            },
        },
    ]

    result = list(filter_by_currency(transactions, "USD"))

    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3


def test_transaction_descriptions() -> None:
    transactions = [
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"},
        {"description": "Оплата услуг"},
    ]

    result = list(transaction_descriptions(transactions))

    assert result == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Оплата услуг",
    ]


def test_card_number_generator() -> None:
    generator = card_number_generator(1, 3)

    result = list(generator)

    assert result == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
    ]


def test_card_number_generator_single() -> None:
    generator = card_number_generator(9999, 9999)

    result = list(generator)

    assert result == [
        "0000 0000 0000 9999",
    ]
