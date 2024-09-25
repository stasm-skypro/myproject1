def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция возвращает список словарей, содержащий только те словари, у которых ключ 'state' соответствует\
    указанному значению в параметре state."""
    if not operations:
        raise ValueError("Список операций не должен быть пустым!")

    return [current_dict for current_dict in operations if current_dict["state"] == state]


def sort_by_date(operations: list[dict], sorting_order: int | bool = 1) -> list[dict]:
    """Функция возвращает новый список, отсортированный по дате."""
    if not operations:
        raise ValueError("Список операций не должен быть пустым!")

    return sorted(operations, key=lambda x: x["date"][:10], reverse=False if sorting_order == 0 else True)


if __name__ == "__main__":
    transaction = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    print(filter_by_state(transaction, "EXECUTED"))
    print(sort_by_date(transaction, 1))
