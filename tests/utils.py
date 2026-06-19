from src.utils import load_transactions


def test_load_transactions_file_not_found() -> None:
    assert load_transactions("unknown.json") == []
