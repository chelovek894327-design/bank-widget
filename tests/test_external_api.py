from unittest.mock import Mock, patch

from src.external_api import transaction_amount


def test_transaction_amount_rub() -> None:
    """
    Проверяет возврат суммы для RUB без обращения к API.
    """
    transaction = {"operationAmount": {"amount": "1000", "currency": {"code": "RUB"}}}

    assert transaction_amount(transaction) == 1000.0


@patch("src.external_api.requests.get")
def test_transaction_amount_usd(mock_get: Mock) -> None:
    """
    Проверяет конвертацию USD в RUB.
    """
    mock_response = Mock()
    mock_response.json.return_value = {"result": 8000.0}
    mock_get.return_value = mock_response

    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}

    assert transaction_amount(transaction) == 8000.0


@patch("src.external_api.requests.get")
def test_transaction_amount_eur(mock_get: Mock) -> None:
    """
    Проверяет конвертацию EUR в RUB.
    """
    mock_response = Mock()
    mock_response.json.return_value = {"result": 9500.0}
    mock_get.return_value = mock_response

    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "EUR"}}}

    assert transaction_amount(transaction) == 9500.0
