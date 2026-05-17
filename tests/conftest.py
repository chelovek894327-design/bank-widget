import pytest


@pytest.fixture
def card_number() -> str:
    return "1234567812345678"


@pytest.fixture
def account_number() -> str:
    return "12345678901234567890"
