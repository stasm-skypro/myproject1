from src.utils import read_file
import pytest


@pytest.mark.parametrize(
    "x, expected",
    [
        ("bad/path", []),
        ("data_for_tests/operations_empty_sample.json", []),
        ("data_for_tests/operations_notlist_sample.json", []),
        (
            "data_for_tests/operations_sample.json",
            [
                {
                    "id": 441945886,
                    "state": "EXECUTED",
                    "date": "2019-08-26T10:50:58.294041",
                    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Maestro 1596837868705199",
                    "to": "Счет 64686473678894779589",
                }
            ],
        ),
    ],
)
def test_read_file(x: str, expected: list):
    assert read_file(x) == expected
