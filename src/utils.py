import json
import logging
import os
import re


# Запуск pytest происходит из корневой директории проекта, а запуск скрипта из директории src.
# Эта конструкция нужна для выравнивания путей.
path = ""
if os.getcwd() == "/Users/stanislavmayatsky/python/Skypro/myprojects/myproject1":
    path = "logs/utils.log"
elif os.getcwd() == "/Users/stanislavmayatsky/python/Skypro/myprojects/myproject1/src":
    path = "../logs/utils.log"

# Базовые настройки логгера
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(path, "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_file(file_path: str) -> list[dict | None]:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Пример использования:
    result = read_file(path_to_operations)
    """
    # Если файл, указанный в переменной file_path не существует, то вернуть пустой список.
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        logger.info(f"Файл {file_path} открыт на чтение.")
    except FileNotFoundError:
        logger.error(f"Файл {file_path} не существует.")
        return []

    # Если json-файл пустой, то вернуть пустой список.
    try:
        data = json.loads(content)
        logger.info(f"Данные из файла {file_path} прочитаны.")
    except json.JSONDecodeError:
        logger.error(f"Ошибка чтения json из файла {file_path}.")
        return []

    # Если содержимое файла не является списком (содержит несписок), то вернуть пустой список.
    if not isinstance(data, list):
        logger.error(f"одержимое файла {file_path} не является объектом типа list.")
        return []

    return data


def find_transactions(transactions_list: list[dict], key_string: str) -> list[dict]:
    """Принимает список словарей с данными о банковских операциях и строку поиска. Возвращает список словарей, у \
    которых в описании есть данная строка."""
    templates = [
        "Перевод с карты на карту",
        "Перевод организации",
        "Перевод со счета на счет",
        "Открытие вклада",
        "Перевод с карты на счет",
    ]
    key_list = []
    pattern = re.compile(key_string)
    for temp in templates:
        if re.search(pattern, temp):
            key_list.append(temp)

    filtered_transactions_list = []
    for key in key_list:
        for transaction in transactions_list:
            if transaction.get("description") != key:
                continue
            filtered_transactions_list.append(transaction)

    return filtered_transactions_list


def filter_transactions_by_category(transactions_list: list[dict]) -> dict:
    """Принимает список словарей с данными о банковских операциях и список категорий операций, а возвращать словарь, \
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории."""
    grouped_transactions = {}
    for transaction in transactions_list:
        category = transaction.get("description")
        if category is not None:
            if category not in grouped_transactions:
                grouped_transactions[category] = 0
            grouped_transactions[category] += 1

    return grouped_transactions


if __name__ == "__main__":
    transactions = read_file("../data/operations.json")
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
    #         "id": 587085106,
    #         "state": "EXECUTED",
    #         "date": "2018-03-23T10:45:06.972075",
    #         "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
    #         "description": "Открытие вклада",
    #         "to": "Счет 41421565395219882431",
    #     },
    #     {
    #         "id": 142264268,
    #         "state": "EXECUTED",
    #         "date": "2019-04-04T23:20:05.206878",
    #         "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
    #         "description": "Перевод со счета на счет",
    #         "from": "Счет 19708645243227258542",
    #         "to": "Счет 75651667383060284188",
    #     },
    #     {
    #         "id": 895315941,
    #         "state": "EXECUTED",
    #         "date": "2018-08-19T04:27:37.904916",
    #         "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
    #         "description": "Перевод с карты на карту",
    #         "from": "Visa Classic 6831982476737658",
    #         "to": "Visa Platinum 8990922113665229",
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
    # ]

    print(find_transactions(transactions, "Перевод с карты на карту"))
    # print(find_transactions(transactions, "Перевод организации"))
    # print(find_transactions(transactions, "Перевод со счета на счет"))
    # print(find_transactions(transactions, "Открытие вклада"))
    # print(find_transactions(transactions, "Перевод с карты на счет"))
    # print(find_transactions(transactions, "Перевод с карты"))
    # print(find_transactions(transactions, "Перевод"))

    print(filter_transactions_by_category(transactions))
