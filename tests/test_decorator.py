from time import sleep
from typing import Any

import pytest

from src.decorators import log


def my_func1(x: str, y: str) -> str:
    """Возвращает бинарную сумму двух чисел."""
    return bin(int(x, 2) + int(y, 2))


def my_func2(interval: int) -> str:
    """Спит заданное время."""
    sleep(interval)
    return f"I sleep in {interval} times."


def test_log11() -> None:
    """Проверяет декоратор log при возникновении исключения.."""
    with pytest.raises(TypeError, match=r".*Неверный тип или количество аргументов.*"):
        log()(my_func1)(1111111111, "00000000000")


def test_log12() -> None:
    """Проверяет что декоратор log записывает в файл сообщение при возникновении исключения."""
    with pytest.raises(TypeError, match=r".*Неверный тип или количество аргументов.*"):
        log("logs/sample.log")(my_func1)(1111111111, "00000000000")

    with open("logs/sample.log", "r", encoding="utf-8") as file:
        content = file.readlines()
        assert (
            content[-1]
            == "my_func1 error: Неверный тип или количество аргументов. Inputs: (1111111111, '00000000000')\n"
        )


def test_log2() -> None:
    """Проверяет декоратор log при возникновении исключения."""
    with pytest.raises(TypeError, match=r".*Неверный тип или количество аргументов.*"):
        log()(my_func2)("1")


def test_log3() -> None:
    """Проверяет декоратор log при возникновении исключения."""
    with pytest.raises(TypeError, match=r".*Неверный тип или количество аргументов.*"):
        log()(my_func1)("1111111111", "00000000000", "111111111")


def test_log4() -> None:
    """Проверяет декоратор log при возникновении исключения."""
    with pytest.raises(TypeError, match=r".*Неверный тип или количество аргументов.*"):
        log()(my_func2)(1, 2)


def test_log_stdout11(capsys: Any) -> None:
    """Проверяет что декоратор log выводит в консоль сообщение при успешном выполнении."""
    log()(my_func1)("1111111111", "00000000000")
    captured = capsys.readouterr()
    assert captured.out == "my_func1 OK, результат: 0b1111111111\n"


def test_log_stdout12(capsys: Any) -> None:
    """Проверяет что декоратор log записывает в файл сообщение при успешном выполнении."""
    log("logs/sample.log")(my_func1)("1111111111", "00000000000")
    captured = capsys.readouterr()
    assert captured.out == "my_func1 OK, результат: 0b1111111111\n"

    with open("logs/sample.log", "r", encoding="utf-8") as file:
        content = file.readlines()
        print(content[-1])
        assert content[-1] == "my_func1 OK, результат: 0b1111111111\n"


def test_log_stdout2(capsys: Any) -> None:
    """Проверяет что декоратор log выводит в консоль сообщение при успешном выполнении."""
    log()(my_func2)(1)
    captured = capsys.readouterr()
    assert captured.out == "my_func2 OK, результат: I sleep in 1 times.\n"
