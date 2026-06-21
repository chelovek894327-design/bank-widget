from unittest.mock import patch

import pandas as pd

from src.readers import read_csv_transactions, read_excel_transactions


@patch("src.readers.pd.read_csv")
def test_read_csv_transactions(mock_read_csv):
    """Тест чтения CSV-файла."""

    dataframe = pd.DataFrame(
        [
            {"id": 1, "amount": 100},
            {"id": 2, "amount": 200},
        ]
    )

    mock_read_csv.return_value = dataframe

    result = read_csv_transactions("transactions.csv")

    assert result == [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 200},
    ]

    mock_read_csv.assert_called_once_with("transactions.csv")


@patch("src.readers.pd.read_excel")
def test_read_excel_transactions(mock_read_excel):
    """Тест чтения Excel-файла."""

    dataframe = pd.DataFrame(
        [
            {"id": 1, "amount": 100},
            {"id": 2, "amount": 200},
        ]
    )

    mock_read_excel.return_value = dataframe

    result = read_excel_transactions("transactions.xlsx")

    assert result == [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 200},
    ]

    mock_read_excel.assert_called_once_with("transactions.xlsx")
