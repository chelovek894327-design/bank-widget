from collections.abc import Generator


def filter_by_currency(
    transactions: list[dict], currency: str
) -> Generator[dict, None, None]:
    """
    Фильтрует транзакции по валюте операции.

    Args:
        transactions: Список транзакций.
        currency: Код валюты (например, USD).

    Yields:
        Транзакции с указанной валютой.
    """
    for transaction in transactions:
        operation_amount = transaction.get("operationAmount", {})
        currency_data = operation_amount.get("currency", {})

        if currency_data.get("code") == currency:
            yield transaction


def transaction_descriptions(
    transactions: list[dict],
) -> Generator[str, None, None]:
    """
    Генератор описаний транзакций.

    Args:
        transactions: Список словарей с транзакциями.

    Yields:
        Описание каждой транзакции.
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(
    start: int, stop: int
) -> Generator[str, None, None]:
    """
    Генератор номеров банковских карт.

    Генерирует номера карт в формате:
    XXXX XXXX XXXX XXXX

    Args:
        start: Начальное значение диапазона.
        stop: Конечное значение диапазона.

    Yields:
        Номер карты в формате XXXX XXXX XXXX XXXX.
    """
    for number in range(start, stop + 1):
        card_number = str(number).zfill(16)

        formatted_number = (
            f"{card_number[0:4]} "
            f"{card_number[4:8]} "
            f"{card_number[8:12]} "
            f"{card_number[12:16]}"
        )

        yield formatted_number
