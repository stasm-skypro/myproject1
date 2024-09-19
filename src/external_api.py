import json
import os
from typing import Any

import requests
from dotenv import load_dotenv

# Загрузка переменных из .env-файла и получение значения API_KEY
load_dotenv()
API_KEY = os.getenv("API_KEY")


def convert_to(value: float, from_currency: str, to_currency: str = "RUB") -> float | str:
    """Принимает значение (value, тип float), исходный код валюты (from_currency, тип str) и желаемый код валюты
     (to_currency тип str) и возвращает значение после конвертации. Использует Exchange Rates Data API.
    Пример использования:
    print(convert_to(100, "USD"))
    """
    if from_currency == "RUB":
        return value

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={value}"
    payload: dict[Any, Any] = {}
    headers = {"apikey": API_KEY}

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = json.loads(response.text)["info"]["rate"]

    # Если запрос обработан успешно (код 200), то возвращаем значение валюты после конвертации.
    if status_code == 200:
        return float(result)
    # Иначе возвращаем причину ошибки.
    else:
        return response.reason


# if __name__ == "__main__":
#     print(convert_to(100, "USD"))
