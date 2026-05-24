from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """
    Декоратор для логирования выполнения функций.

    Args:
        filename: Имя файла для записи логов.
                  Если None — вывод в консоль.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)

                message = (
                    f"{func.__name__} ok. "
                    f"Result: {result}"
                )

                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(message + "\n")
                else:
                    print(message)

                return result

            except Exception as error:
                message = (
                    f"{func.__name__} error: "
                    f"{type(error).__name__}. "
                    f"Inputs: args={args}, kwargs={kwargs}"
                )

                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(message + "\n")
                else:
                    print(message)

                raise

        return wrapper

    return decorator
