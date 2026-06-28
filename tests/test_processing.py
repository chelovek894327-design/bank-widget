from src.processing import filter_by_state, sort_by_date


def test_filter_by_state() -> None:
    data = [{"state": "EXECUTED"}, {"state": "CANCELED"}]
    assert len(filter_by_state(data, "EXECUTED")) == 1


def test_sort_by_date() -> None:
    data = [{"date": "2020"}, {"date": "2021"}]
    result = sort_by_date(data)
    assert result[0]["date"] == "2021"
