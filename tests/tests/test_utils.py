import json

from src.utils import load_transactions


def test_load_transactions_success(tmp_path) -> None:
    """
    Проверяет успешную загрузку транзакций.
    """
    file = tmp_path / "test.json"

    data = [{"id": 1}, {"id": 2}]

    file.write_text(json.dumps(data), encoding="utf-8")

    assert load_transactions(str(file)) == data


def test_load_transactions_file_not_found() -> None:
    """
    Проверяет обработку отсутствующего файла.
    """
    assert load_transactions("unknown.json") == []


def test_load_transactions_not_list(tmp_path) -> None:
    """
    Проверяет обработку JSON, который не является списком.
    """
    file = tmp_path / "test.json"

    file.write_text('{"id": 1}', encoding="utf-8")

    assert load_transactions(str(file)) == []


def test_load_transactions_empty_file(tmp_path) -> None:
    """
    Проверяет обработку пустого файла.
    """
    file = tmp_path / "empty.json"

    file.write_text("", encoding="utf-8")

    assert load_transactions(str(file)) == []
