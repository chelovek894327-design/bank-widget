from typing import Any, Dict, List


def filter_by_state(
    operations: List[Dict[str, Any]], state: str = "EXECUTED"
) -> List[Dict[str, Any]]:
    """Фильтрует список операций по значению ключа 'state'."""
    return [operation for operation in operations if operation.get("state") == state]


def sort_by_date(
    operations: List[Dict[str, Any]], descending: bool = True
) -> List[Dict[str, Any]]:
    """Сортирует список операций по дате."""
    return sorted(
        operations,
        key=lambda operation: operation.get("date", ""),
        reverse=descending,
    )

