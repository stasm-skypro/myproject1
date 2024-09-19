from typing import Generator


def filter_by_currency(transaction_list: list[dict], currency_code: str) -> Generator:
    """Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной \
    (например, USD)."""
    for transaction in transaction_list:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transaction_list: list[dict]) -> Generator:
    """Возвращает по очереди описание каждой операции из списка transaction_list."""
    for transaction in transaction_list:
        yield transaction["description"]


def card_number_generator(start_from: str) -> Generator:
    """Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    <Реализация генератора:
        g = card_number_generator()
        for i in range(k):  #где к в диапазоне от 1 до 39997: (9999 x 4) + 1
            print(next(g))>"""
    start_from_number = int(start_from.replace(" ", ""))
    # диапазон номеров внутри одного блока 1 - 9999 включительно
    while 1:
        card_number = f"{start_from_number:016}"
        yield " ".join([card_number[pos : pos + 4] for pos in range(0, 16, 4)])
        start_from_number += 1
