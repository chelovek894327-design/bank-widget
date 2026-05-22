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