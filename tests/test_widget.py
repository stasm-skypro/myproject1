import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "x, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Счет 64686473678894779589", "Счет **9589"),
    ],
)
def test_mask_account_card(x: str, expected: str) -> None:
    """Тестируем функцию mask_account_card - корректные входные данные."""
    assert mask_account_card(x) == expected


def test_test_mask_account_card_rise_exception11() -> None:
    """Тестируем функцию mask_account_card - поле с номером карты пустое."""
    with pytest.raises(ValueError, match="Поле с номером карты или номером счёта не должно быть пустым!"):
        mask_account_card("")


def test_test_mask_account_card_rise_exception12() -> None:
    """Тестируем функцию mask_account_card - поле с номером карты пустое."""
    with pytest.raises(ValueError, match="Поле с номером карты или номером счёта не должно быть пустым!"):
        mask_account_card(" ")


def test_test_mask_account_card_rise_exception13() -> None:
    """Тестируем функцию mask_account_card - поле с номером карты неправильно заполнено."""
    with pytest.raises(ValueError, match="Поле карты должно быть правильно заполнено!"):
        mask_account_card("Ma stro 1596837868705199")


def test_test_mask_account_card_rise_exception14() -> None:
    """Тестируем функцию mask_account_card - поле с номером карты неправильно заполнено."""
    with pytest.raises(ValueError, match="Поле карты должно быть правильно заполнено!"):
        mask_account_card("Visa-Classic 1596837868705199")


def test_test_mask_account_card_rise_exception15() -> None:
    """Тестируем функцию mask_account_card - поле с номером карты неправильно заполнено."""
    with pytest.raises(ValueError, match="Поле карты должно быть правильно заполнено!"):
        mask_account_card("VisaClassic 1596837868705199")


def test_test_mask_account_card_rise_exception16() -> None:
    """Тестируем функцию mask_account_card - поле с номером карты неправильно заполнено."""
    with pytest.raises(ValueError, match="Поле карты должно быть правильно заполнено!"):
        mask_account_card("VC 1596837868705199")


def test_test_mask_account_card_rise_exception21() -> None:
    """Тестируем функцию mask_account_card - поле с номером карты неправильно заполнено."""
    with pytest.raises(ValueError, match="Номер карты должен содержать цифры от 0 до 9"):
        mask_account_card("Visa Classic")


def test_test_mask_account_card_rise_exception25() -> None:
    """Тестируем функцию mask_account_card - поле с номером карты неправильно заполнено."""
    with pytest.raises(ValueError, match="Номер карты должен содержать цифры от 0 до 9"):
        mask_account_card("Visa Classic ")


@pytest.mark.parametrize(
    "x, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("1024-01-01T02:26:18.671407", "01.01.1024"),
    ],
)
def test_get_date(x: str, expected: str) -> None:
    """Тестируем функцию get_date - стандартные входные данные."""
    assert get_date(x) == expected
