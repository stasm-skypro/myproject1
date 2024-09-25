import json
import os
from typing import Any

import requests
from dotenv import load_dotenv

# Загрузка переменных из .env-файла и получение значения API_KEY
load_dotenv()
API_KEY = os.getenv("API_KEY")


def _convert_to(value: float, from_currency: str, to_currency: str = "RUB") -> float | str:
    """Принимает значение (value, тип float), исходный код валюты (from_currency, тип str) и желаемый код валюты
     (to_currency тип str) и возвращает значение после конвертации. Использует Exchange Rates Data API.
    Пример использования:
    print(convert_to(100, "USD"))
    """
    # -----------------------------------------------------------------------------------------------------------------
    # url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={value}"
    # -----------------------------------------------------------------------------------------------------------------
    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload: dict[Any, Any] = {"amount": str(value), "from": from_currency, "to": to_currency}
    headers = {"apikey": API_KEY}

    response = requests.request("GET", url, headers=headers, params=payload)

    status_code = response.status_code
    # Если запрос обработан успешно (код 200), то возвращаем значение валюты после конвертации.
    if status_code == 200:
        result = json.loads(response.text)["info"]["rate"]
        return float(result)

    # Иначе возвращаем причину ошибки.
    else:
        return response.reason


def convert_to_rub(transaction: dict) -> float | str:
    """Принимает на вход транзакцию и возвращает сумму транзакции в рублях.
    Пример использования:
    amount = convert_to_rub(current_transaction)
    print(amount)
    """
    from_currency = transaction["operationAmount"]["currency"]["code"]
    # Если сумма (amount) внутри трансакции уже в рублях, то конвертация не нужна, возвращаем сумму.
    if from_currency == "RUB":
        return float(transaction["operationAmount"]["amount"])

    # Иначе обращаемся к внешнему API за конвертацией.
    else:
        return _convert_to(
            transaction["operationAmount"]["amount"], transaction["operationAmount"]["currency"]["code"]
        )


if __name__ == "__main__":
    current_transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    print(convert_to_rub(current_transaction))

    current_transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
    print(convert_to_rub(current_transaction))
