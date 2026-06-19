import json
import logging
from pathlib import Path

log_dir = Path(__file__).resolve().parent.parent / "logs"
log_dir.mkdir(exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

if not logger.handlers:
    file_handler = logging.FileHandler(
        log_dir / "utils.log",
        mode="w",
        encoding="utf-8",
    )

    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)


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
            logger.info(f"Успешно загружено {len(data)} транзакций")
            return data

        logger.error("JSON не содержит список транзакций")
        return []

    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
        return []

    except json.JSONDecodeError:
        logger.error(f"Ошибка чтения JSON: {file_path}")
        return []