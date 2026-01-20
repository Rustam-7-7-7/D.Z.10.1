import os

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_to_rubles(transaction):
    ''' Функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount)
         в рублях, тип данных — float. Если транзакция была в USD или EUR, происходит обращение к
          внешнему API для получения текущего курса валют и конвертации суммы операции в рубли. '''

    amount = float(transaction['operationAmount']['amount'])
    currency = transaction['operationAmount']['currency']['code']

    if currency == 'RUB':
        return round(amount, 2)

    api_key = os.getenv("API_KEY")
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

    headers = {
        "apikey": api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Ошибка запроса: {response.status_code}")
        return None

    data = response.json()

    if 'result' not in data:
        print("Ошибка в данных ответа API")
        return None

    amount_in_rubles = data['result']

    return round(float(amount_in_rubles), 2)


# Пример транзакции
transaction = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
        "amount": "1000",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
}

rubles = convert_to_rubles(transaction)
if rubles is not None:
    print(rubles)
