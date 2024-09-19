import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def collect() -> list:
    """Хук для тестов функции filter_by_currency из модуля generators"""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },  # USD 1
        {
            "id": 15020681,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод с карты на карту",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },  # EUR 1
        {
            "id": 26131791,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },  # RUB 1
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },  # USD 2
        {
            "id": 253375379,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },  # EUR 2
        {
            "id": 364486480,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод с карты на карту",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },  # RUB 2
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },  # USD 3
        {
            "id": 906426052,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод со счета на счет",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },  # EUR 3
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },  # RUB 3
    ]


def test_filter_by_currency11(collect: list) -> None:
    """Тестирование функции filter_by_currency с параметром USD."""
    g = filter_by_currency(collect, "USD")
    assert next(g) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }  # USD 1
    assert next(g) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }  # USD 2
    assert next(g) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }  # USD 3


def test_filter_by_currency12(collect: list) -> None:
    """Тестирование функции filter_by_currency с параметром EUR."""
    g = filter_by_currency(collect, "EUR")
    assert next(g) == {
        "id": 15020681,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод с карты на карту",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }  # EUR 1
    assert next(g) == {
        "id": 253375379,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }  # EUR 2
    assert next(g) == {
        "id": 906426052,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод со счета на счет",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }  # EUR 3


def test_filter_by_currency13(collect: list) -> None:
    """Тестирование функции filter_by_currency с параметром RUR."""
    g = filter_by_currency(collect, "RUB")
    assert next(g) == {
        "id": 26131791,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }  # RUB 1
    assert next(g) == {
        "id": 364486480,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод с карты на карту",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }  # RUB 2
    assert next(g) == {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    }  # RUB 3


def test_transaction_descriptions(collect: list) -> None:
    """Тестирование функции transaction_descriptions."""
    g = transaction_descriptions(collect)
    assert next(g) == "Перевод организации"  # USD 1
    assert next(g) == "Перевод с карты на карту"  # EUR 1
    assert next(g) == "Перевод организации"  # RUB 1
    assert next(g) == "Перевод со счета на счет"  # USD 2
    assert next(g) == "Перевод со счета на счет"  # EUR 2
    assert next(g) == "Перевод с карты на карту"  # RUB 2
    assert next(g) == "Перевод с карты на карту"  # USD 3
    assert next(g) == "Перевод со счета на счет"  # EUR 3
    assert next(g) == "Перевод организации"  # RUB 3


def test_card_number_generator1() -> None:
    """Тестирование функции card_number_generator."""
    g = card_number_generator("0000 0000 0000 0001")
    expected = iter(
        [
            "0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003",
            "0000 0000 0000 0004",
            "0000 0000 0000 0005",
        ]
    )
    for i in range(5):
        assert next(g) == next(expected)


def test_card_number_generator2() -> None:
    """Тестирование функции card_number_generator."""
    g = card_number_generator("0000 0000 0001 0000")
    expected = iter(
        [
            "0000 0000 0001 0000",
            "0000 0000 0001 0001",
            "0000 0000 0001 0002",
            "0000 0000 0001 0003",
            "0000 0000 0001 0004",
        ]
    )
    for i in range(5):
        assert next(g) == next(expected)


def test_card_number_generator3() -> None:
    """Тестирование функции card_number_generator."""
    g = card_number_generator("9999 9999 9999 9995")
    expected = iter(
        [
            "9999 9999 9999 9995",
            "9999 9999 9999 9996",
            "9999 9999 9999 9997",
            "9999 9999 9999 9998",
            "9999 9999 9999 9999",
        ]
    )
    for i in range(5):
        assert next(g) == next(expected)
