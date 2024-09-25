from src.external_api import convert_to_rub
from src.processing import filter_by_state, sort_by_date
from src.utils import read_file
from src.widget import get_date, mask_account_card


def pretty_print(lst: list) -> None:
    """Функция распечатывает двумерный список по-строчно."""
    for row in lst:
        print(row)


if __name__ == "__main__":
    print(mask_account_card.__name__)
    print(mask_account_card.__doc__)
    print(mask_account_card("Visa Platinum 8990922113665229"))
    print(mask_account_card("Visa 8990922113665229"))
    print(mask_account_card("Visa 89909221136652"))
    print(mask_account_card("VP 8990922113665229"))
    print(mask_account_card("8990922113665229"))
    print(mask_account_card("Visa 899092211a66522?"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(mask_account_card("Счет 736541084301358743"))
    print(mask_account_card("73654108430135874305"))
    print(mask_account_card("Счет 73.54108430g3587430?"))
    print(mask_account_card("Счет"))
    print(mask_account_card("Счет "))
    print(mask_account_card(""))

    print(mask_account_card.__name__)
    print(get_date.__doc__)
    print(get_date("2024-03-11T02:26:18.671407"))

    print(mask_account_card.__name__)
    print(filter_by_state.__doc__)
    pretty_print(
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
        )
    )

    print(mask_account_card.__name__)
    print(sort_by_date.__doc__)
    pretty_print(
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )

    current_transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    print("RUB:", convert_to_rub(current_transaction))

    current_transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
    print("USD:", convert_to_rub(current_transaction))

    current_transaction = {
        "id": 490100847,
        "state": "EXECUTED",
        "date": "2018-12-22T02:02:49.564873",
        "operationAmount": {"amount": "56516.63", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Gold 8326537236216459",
        "to": "MasterCard 6783917276771847",
    }
    print("EUR:", convert_to_rub(current_transaction))

    path_to_operations = "../data/operations.json"
    result = read_file(path_to_operations)
    print(result)

    current_transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
