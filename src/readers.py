import pandas as pd


def read_csv_transactions(file_path: str) -> list[dict]:
    """
    Считывает финансовые операции из CSV-файла.

    Args:
        file_path: Путь к CSV-файлу.

    Returns:
        Список словарей с транзакциями.
    """
    dataframe = pd.read_csv(file_path)
    return dataframe.to_dict(orient="records")


def read_excel_transactions(file_path: str) -> list[dict]:
    """
    Считывает финансовые операции из Excel-файла.

    Args:
        file_path: Путь к Excel-файлу.

    Returns:
        Список словарей с транзакциями.
    """
    dataframe = pd.read_excel(file_path)
    return dataframe.to_dict(orient="records")
