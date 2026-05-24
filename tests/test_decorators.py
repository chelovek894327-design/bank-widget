import pytest

from src.decorators import log


@log()
def add(a: int, b: int) -> int:
    """
    Складывает два числа.

    Args:
        a: Первое число.
        b: Второе число.

    Returns:
        Сумма двух чисел.
    """
    return a + b


@log()
def divide(a: int, b: int) -> float:
    """
    Делит одно число на другое.

    Args:
        a: Делимое.
        b: Делитель.

    Returns:
        Результат деления.

    Raises:
        ZeroDivisionError: Если b равно 0.
    """
    return a / b


def test_log_success(capsys: pytest.CaptureFixture[str]) -> None:
    """
    Проверяет успешное логирование функции.
    """
    add(2, 3)

    captured = capsys.readouterr()

    assert "add ok. Result: 5" in captured.out


def test_log_error(capsys: pytest.CaptureFixture[str]) -> None:
    """
    Проверяет логирование ошибки.
    """
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()

    assert "divide error: ZeroDivisionError" in captured.out


def test_log_to_file(tmp_path) -> None:
    """
    Проверяет запись логов в файл.
    """
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def multiply(a: int, b: int) -> int:
        """
        Умножает два числа.

        Args:
            a: Первое число.
            b: Второе число.

        Returns:
            Результат умножения.
        """
        return a * b

    multiply(2, 4)

    content = log_file.read_text(encoding="utf-8")

    assert "multiply ok. Result: 8" in content
