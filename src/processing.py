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
