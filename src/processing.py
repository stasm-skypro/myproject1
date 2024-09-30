import re
from src.utils import read_file
from collections import Counter
import os
import logging

# Запуск pytest происходит из корневой директории проекта, а запуск скрипта из директории src.
# Эта конструкция нужна для выравнивания путей.
path = ""
if os.getcwd() == "/Users/stanislavmayatsky/python/Skypro/myprojects/myproject1":
    path = "logs/processing.log"
elif os.getcwd() == "/Users/stanislavmayatsky/python/Skypro/myprojects/myproject1/src":
    path = "../logs/processing.log"

# Базовые настройки логгера
logger = logging.getLogger("processing")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(path, "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def filter_by_state(transactions_list: list, state: str = "EXECUTED") -> list:
    """Функция возвращает список словарей, содержащий только те словари, у которых ключ 'state' соответствует\
    указанному значению в параметре state."""
    if not transactions_list:
        logger.error(f"Передан пустой список операций {transactions_list}.")
        raise ValueError("Список операций не должен быть пустым!")

    result = []
    for transaction in transactions_list:
        if transaction == {}:
            continue
        if transaction["state"] == state:
            result.append(transaction)

    logger.info(f"Список операций успешно отфильтрован по статусу {state}.")
    return result


def filter_by_rub(transactions_list: list) -> list:
    """Функция возвращает список словарей, содержащий только те словари, у которых ключ 'code' равен RUB."""
    if not transactions_list:
        logger.error(f"Передан пустой список операций {transactions_list}.")
        raise ValueError("Список операций не должен быть пустым!")

    result = []
    for transaction in transactions_list:
        if transaction == {}:
            continue
        if transaction["operationAmount"]["currency"]["code"] == "RUB":
            result.append(transaction)

    logger.info("Список операций успешно отфильтрован по ключу code=RUB.")
    return result


def sort_by_date(transactions_list: list, sorting_order: int | bool = 1) -> list:
    """Функция возвращает новый список, отсортированный по дате."""
    if not transactions_list:
        logger.error(f"Передан пустой список операций {transactions_list}.")
        raise ValueError("Список операций не должен быть пустым!")

    logger.info(
        f"Список операций успешно отфильтрован по дате {'по убыванию' if sorting_order else 'по возрастанию'}."
    )
    return sorted(
        transactions_list,
        key=lambda x: x["date"][:10] if x != {} else "",
        reverse=False if sorting_order == 0 else True,
    )


def find_transactions(transactions_list: list, key_string: str) -> list:
    """Принимает список словарей с данными о банковских операциях и строку поиска. Возвращает список словарей, у \
    которых в описании есть данная строка."""
    templates = [
        "перевод с карты на карту",
        "перевод организации",
        "перевод со счета на счет",
        "открытие вклада",
        "перевод с карты на счет",
    ]
    key_list = []
    pattern = re.compile(key_string.lower())
    for temp in templates:
        if re.search(pattern, temp):
            key_list.append(temp)

    filtered_transactions_list = []
    for key in key_list:
        for transaction in transactions_list:
            if transaction == {}:
                continue
            if transaction["description"].lower() != key:
                continue
            filtered_transactions_list.append(transaction)

    logger.info(f"Список операций успешно отфильтрован по описанию {key_string}.")
    return filtered_transactions_list


def group_transactions_by_category(transactions_list: list) -> dict:
    """Принимает список словарей с данными о банковских операциях и список категорий операций, а возвращать словарь, \
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории."""
    description_list = [
        transaction.get("description")
        for transaction in transactions_list
        if transaction.get("description") is not None
    ]
    grouped_transactions = Counter(description_list)

    logger.info("Список операций успешно сгрупирован по названиям категорий.")
    return dict(grouped_transactions)


if __name__ == "__main__":
    # transactions = [
    #     {
    #         "id": 441945886,
    #         "state": "EXECUTED",
    #         "date": "2019-08-26T10:50:58.294041",
    #         "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
    #         "description": "Перевод организации",
    #         "from": "Maestro 1596837868705199",
    #         "to": "Счет 64686473678894779589",
    #     },
    #     {
    #         "id": 615064591,
    #         "state": "CANCELED",
    #         "date": "2018-10-14T08:21:33.419441",
    #         "operationAmount": {"amount": "77751.04", "currency": {"name": "руб.", "code": "RUB"}},
    #         "description": "Перевод с карты на счет",
    #         "from": "Maestro 3928549031574026",
    #         "to": "Счет 84163357546688983493",
    #     },
    #     {},
    # ]
    transactions = read_file("../data/operations.json")
    # transactions = read_file("../data/transactions.csv")
    # transactions = read_file("../data/transactions_excel.xlsx")
    # print(transactions)
    # print(filter_by_state(transactions, "EXECUTED"))
    # print(sort_by_date(transactions, 1))

    # print(find_transactions(transactions, "Перевод с карты на карту"))
    # print(find_transactions(transactions, "Перевод организации"))
    # print(find_transactions(transactions, "Перевод со счета на счет"))
    # print(find_transactions(transactions, "Открытие вклада"))
    # print(find_transactions(transactions, "Перевод с карты на счет"))
    # print(find_transactions(transactions, "Перевод с карты"))
    print(find_transactions(transactions, "Перевод"))

    print(group_transactions_by_category(transactions))
