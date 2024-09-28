import json
import logging
import os
import re

from mypyc.irbuild.prepare import prepare_methods_and_attributes

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


def filter_transactions_by_category(transactions_list: list[dict]) -> list[dict]:
    """Принимает список словарей с данными о банковских операциях и список категорий операций, а возвращать словарь, \
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории."""
    pass


if __name__ == "__main__":
    transactions = read_file("../data/operations.json")
    # print(find_transactions(transactions, "Перевод с карты на карту"))
    # print(find_transactions(transactions, "Перевод организации"))
    # print(find_transactions(transactions, "Перевод со счета на счет"))
    # print(find_transactions(transactions, "Открытие вклада"))
    # print(find_transactions(transactions, "Перевод с карты на счет"))
    # print(find_transactions(transactions, "Перевод с карты"))
    print(find_transactions(transactions, "Перевод"))
