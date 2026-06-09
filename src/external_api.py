import os

import requests
from dotenv import load_dotenv

load_dotenv()


def transaction_amount(transaction: dict) -> float:
    """
    Возвращает сумму транзакции в рублях.

    Args:
        transaction: Словарь транзакции.

    Returns:
        Сумма в рублях.
    """
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    api_key = os.getenv("API_KEY")
    if api_key is None:
        raise ValueError("API_KEY not found")

    response = requests.get(
        "https://api.apilayer.com/exchangerates_data/convert",
        headers={"apikey": api_key},
        params={
            "from": currency,
            "to": "RUB",
            "amount": amount,
        },
        timeout=10,
    )

    result = response.json()

    return float(result["result"])
