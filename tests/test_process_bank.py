import pytest

from src.process_bank import process_bank_search, process_bank_operations


@pytest.fixture
def data():
    return [
        {'id': 1245327.0, 'state': 'PENDING', 'date': '2021-03-09T00:56:48Z', 'amount': 24252.0,
         'currency_name': 'Somoni',
         'currency_code': 'TJS', 'from': 'Discover 3233958335206913', 'to': 'Visa 6269545625045856',
         'description': 'Перевод с карты на карту'},
        {'id': 134341.0, 'state': 'CANCELED', 'date': '2022-03-03T08:41:08Z', 'amount': 13642.0,
         'currency_name': 'Peso',
         'currency_code': 'COP', 'from': 'Visa 9770850749183268', 'to': 'American Express 0522499169905654',
         'description': 'Перевод с карты на карту'},
        {'id': 2177828.0, 'state': 'EXECUTED', 'date': '2022-04-14T15:14:21Z', 'amount': 24853.0,
         'currency_name': 'Yuan Renminbi', 'currency_code': 'CNY', 'from': 'Счет 38577962752140632721',
         'to': 'Счет 47657753885349826314', 'description': 'Перевод со счета на счет'},
        {'id': 4137938.0, 'state': 'EXECUTED', 'date': '2023-01-04T13:13:34Z', 'amount': 15560.0,
         'currency_name': 'Real',
         'currency_code': 'BRL', 'from': 'nan', 'to': 'Счет 38164279390569873521', 'description': 'Открытие вклада'},
        {'id': 4699552.0, 'state': 'EXECUTED', 'date': '2022-03-23T08:29:37Z', 'amount': 23423.0,
         'currency_name': 'Peso',
         'currency_code': 'PHP', 'from': 'Discover 7269000803370165', 'to': 'American Express 1963030970727681',
         'description': 'Перевод с карты на карту'}
    ]


def test_process_bank_search(data):
    assert process_bank_search(data, search='вклад') == [
        {'id': 4137938.0, 'state': 'EXECUTED', 'date': '2023-01-04T13:13:34Z', 'amount': 15560.0,
         'currency_name': 'Real', 'currency_code': 'BRL', 'from': 'nan', 'to': 'Счет 38164279390569873521',
         'description': 'Открытие вклада'}
    ]


def test_process_bank_operations(data):
    assert process_bank_operations(data, categories=['Открытие', 'перевод', 'счет']) == {
        'перевод': 4, 'счет': 1, 'открытие': 1
    }
