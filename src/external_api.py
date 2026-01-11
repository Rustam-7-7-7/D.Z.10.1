import os

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_to_rubles(transaction):
    ''' Функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount)
         в рублях, тип данных — float. Если транзакция была в USD или EUR, происходит обращение к
          внешнему API для получения текущего курса валют и конвертации суммы операции в рубли. '''
    amount = transaction['amount']
    currency = transaction['currency']

    if currency == 'RUB':
        return float(amount)

    api_key = os.getenv("API_KEY")
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

    headers = {
        "apikey": api_key
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    amount_in_rubles = data['result']

    return float(amount_in_rubles)


# Пример транзакции
transaction = {'amount': 100, 'currency': 'USD'}
rubles = convert_to_rubles(transaction)
print(rubles)
