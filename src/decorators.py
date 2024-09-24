from typing import Any


def write_log(filename: str, text: str) -> None:
    """Делает запись сообщения text в файл filename.
    Args:
        text - строка, заканчивающуюся символом перевода каретки '\n'
        filename - путь к файлу, в который производится запись."""
    with open(filename, "a", encoding="utf-8") as file:
        file.writelines(text)
    file.close()


def log(filename: str | None = None) -> Any:
    """Логирует начало и конец выполнения функции, её результаты или возникшие ошибки."""

    def outer_wrapper(f: Any) -> Any:

        def inner_wrapper(*args: tuple, **kwargs: dict) -> Any:
            res = None

            try:
                res = f(*args, **kwargs)

            except Exception as e:
                if e:
                    msg = f"{f.__name__} error: Неверный тип или количество аргументов. Inputs: {args}"
                    if filename is not None:
                        write_log(filename, msg + "\n")
                    raise TypeError(msg)

            msg = f"{f.__name__} OK, результат: {res}"
            if filename is not None:
                write_log(filename, msg + "\n")
            print(msg)

            return res

        return inner_wrapper

    return outer_wrapper


if __name__ == "__main__":
    log("../logs/sample.log")
