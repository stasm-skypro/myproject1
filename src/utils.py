import json
from typing import Any

from src.external_api import convert_to


def read_file(file_path: str) -> list[dict | None]:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Пример использования:
    result = read_file(path_to_operations)
    """
    # Если файл, указанный в переменной file_path не существует, то вернуть пустой список.
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        return []

    # Если json-файл пустой, то вернуть пустой список.
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        return []

    # Если содержимое файла не является списком (содержит несписок), то вернуть пустой список.
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


if __name__ == "__main__":
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
    # amount = get_amount(current_transaction)
    # print(amount)
