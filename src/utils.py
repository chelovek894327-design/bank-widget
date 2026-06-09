import json


def load_transactions(file_path: str) -> list[dict]:
    """
    Загружает список транзакций из JSON-файла.

    Args:
        file_path: Путь к JSON-файлу.

    Returns:
        Список транзакций или пустой список.
    """
    try:
        with open(file_path, encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                return data

    except (FileNotFoundError, json.JSONDecodeError):
        pass

    return []
