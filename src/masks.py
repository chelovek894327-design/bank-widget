import logging
from pathlib import Path

log_dir = Path(__file__).resolve().parent.parent / "logs"
log_dir.mkdir(exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

if not logger.handlers:
    file_handler = logging.FileHandler(
        log_dir / "masks.log",
        mode="w",
        encoding="utf-8",
    )

    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты."""
    new_card_number = card_number.replace(" ", "")

    if not new_card_number.isdigit():
        logger.error("Номер карты содержит недопустимые символы")
        return "Формат номера карты неверный, он должен состоять только из цифр."

    if len(new_card_number) != 16:
        logger.error("Некорректная длина номера карты")
        return "Номер карты должен содержать 16 цифр. Попробуйте ещё раз."

    masked_number = (
        f"{new_card_number[:4]} "
        f"{new_card_number[4:6]}** **** "
        f"{new_card_number[-4:]}"
    )

    logger.info("Номер карты успешно замаскирован")
    return masked_number

def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счета."""
    new_account_number = account_number.replace(" ", "")

    if not new_account_number.isdigit():
        logger.error("Номер счета содержит недопустимые символы")
        return "Формат номера счета неверный, он должен состоять только из цифр."

    if len(new_account_number) != 20:
        logger.error("Некорректная длина номера счета")
        return "Номер счета должен содержать 20 цифр. Попробуйте ещё раз."

    masked_account = f"**{new_account_number[-4:]}"

    logger.info("Номер счета успешно замаскирован")
    return masked_account