import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "x, expected",
    [
        ("1111111111111111", "1111 11** **** 1111"),
        ("1001100110011001", "1001 10** **** 1001"),
        ("1001-1001-1001-1001", "1001 10** **** 1001"),
        ("100-11001-100-11001", "1001 10** **** 1001"),
        ("1001 1001 1001 1001", "1001 10** **** 1001"),
        ("1001 1001-1001 1001", "1001 10** **** 1001"),
        ("1001 10011001 10-01", "1001 10** **** 1001"),
    ],
)
def test_get_mask_card_number(x: str, expected: str) -> None:
    """Тестируем функцию get_mask_card_number - номер карты корректный."""
    assert get_mask_card_number(x) == expected


def test_get_mask_card_number_raise_exception1() -> None:
    """Тестируем функцию get_mask_card_number - номер карты менее 16 символов"""
    with pytest.raises(ValueError, match=".* 16 .*"):
        get_mask_card_number("111111111111111")


def test_get_mask_card_number_raise_exception2() -> None:
    """Тестируем функцию get_mask_card_number - номер карты более 16 символов"""
    with pytest.raises(ValueError, match=".* 16 .*"):
        get_mask_card_number("1111111111111111111111")


def test_get_mask_card_number_raise_exception3() -> None:
    """Тестируем функцию get_mask_card_number - номер карты пустой"""
    with pytest.raises(ValueError, match="Номер карты должен содержать цифры от 0 до 9"):
        get_mask_card_number("")


def test_get_mask_card_number_raise_exception4() -> None:
    """Тестируем функцию get_mask_card_number - номер карты содержит недопустимые символы"""
    with pytest.raises(ValueError, match="Номер карты должен содержать цифры от 0 до 9"):
        get_mask_card_number("")


@pytest.mark.parametrize(
    "x, expected",
    [
        ("11111111111111111111", "**1111"),
        ("11001100110011001100", "**1100"),
        ("1100-1100-1100-1100-1100", "**1100"),
        ("110-01100-11001-100-1100", "**1100"),
        ("1100 1100 1100 1100 1100", "**1100"),
        ("1100-1100 1100-1100 1100", "**1100"),
        ("11 00-110011 00-11001100", "**1100"),
    ],
)
def test_get_mask_account(x: str, expected: str) -> None:
    """Тестируем функцию test_get_mask_account - номер счёта правильной длины."""
    assert get_mask_account(x) == expected


def test_get_mask_account_raise_exception1() -> None:
    """Тестируем функцию get_mask_account - номер счёта менее 20 символов"""
    with pytest.raises(ValueError, match=".* 20 .*"):
        get_mask_account("111111111111111")


def test_get_mask_account_raise_exception2() -> None:
    """Тестируем функцию get_mask_account - номер счёта более 20 символов"""
    with pytest.raises(ValueError, match=".* 20 .*"):
        get_mask_account("1111111111111111111111")


def test_get_mask_account_raise_exception3() -> None:
    """Тестируем функцию get_mask_account - номер счёта пустой"""
    with pytest.raises(ValueError, match="Номер счёта должен содержать цифры от 0 до 9"):
        get_mask_account("")


def test_get_mask_account_raise_exception4() -> None:
    """Тестируем функцию get_mask_account - номер счёта содержит недопустимые символы"""
    with pytest.raises(ValueError, match="Номер счёта должен содержать цифры от 0 до 9"):
        get_mask_account("")
