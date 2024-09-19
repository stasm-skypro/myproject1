# Реализуйте функцию, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых
# транзакциях. Если файл пустой, содержит не список или не найден, функция возвращает пустой список. Функцию поместите
# в модуль utils.
# Файл с данными о финансовых транзациях operations.json поместите в директорию data/ в корне проекта.
# Реализуйте функцию, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных
# float. Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют и
# конвертации суммы операции в рубли. Для конвертации валюты воспользуйтесь Exchange Rates Data API:
# https://apilayer.com/exchangerates_data-api. Функцию конвертации поместите в модуль external_api.
# Используйте переменные окружения из файла .env для сокрытия чувствительных данных (токенов доступа для API). Создайте
# шаблон файла .env и разместите в репозитории на GitHub.
import json
from typing import Any

from external_api import convert_to


def read_file(file_path: str) -> list[dict | None]:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Пример использования:
    result = read_file(path_to_operations)
    """
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

        if not file or not content:
            return []

        data = json.loads(content)
        if not isinstance(data, list):
            return []

        return data


def get_amount(transaction: dict) -> float | Any:
    """Принимает на вход транзакцию и возвращает сумму транзакции в рублях.
    Пример использования:
    amount = get_amount(current_transaction)
    """
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return transaction["operationAmount"]["amount"]
    else:
        return convert_to(transaction["operationAmount"]["amount"], transaction["operationAmount"]["currency"]["code"])


# if __name__ == "__main__":
#     path_to_operations = "../data/operations.json"
#     result = read_file(path_to_operations)
#     print(result)
#
#     current_transaction = {
#         "id": 41428829,
#         "state": "EXECUTED",
#         "date": "2019-07-03T18:35:29.512364",
#         "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод организации",
#         "from": "MasterCard 7158300734726758",
#         "to": "Счет 35383033474447895560",
#     }
#     amount = get_amount(current_transaction)
#     print(amount)
