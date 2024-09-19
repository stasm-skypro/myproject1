from src.processing import filter_by_state, sort_by_date
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
    print(mask_account_card("VP 8990922113665229"))
    print(mask_account_card("8990922113665229"))
    print(mask_account_card("Счет 73654108430135874305"))
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
