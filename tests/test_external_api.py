import unittest
from unittest.mock import Mock, patch

from src.external_api import convert_to_rubles


class TestConvertToRubles(unittest.TestCase):

    @patch('src.external_api.requests.get')
    def test_convert_usd_to_rubles(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {'result': 75000.0}

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

        result = convert_to_rubles(transaction)
        self.assertEqual(result, 75000.0)

    @patch('src.external_api.requests.get')
    def test_convert_eur_to_rubles(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {'result': 88000.0}

        transaction = {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "1000",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }

        result = convert_to_rubles(transaction)
        self.assertEqual(result, 88000.0)

    @patch('src.external_api.requests.get')
    def test_convert_rub_to_rubles(self, mock_get):
        transaction = {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "1000",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }

        result = convert_to_rubles(transaction)
        self.assertEqual(result, 1000.0)

    @patch('src.external_api.requests.get')
    def test_api_error(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 500
        mock_response.json.return_value = {}

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

        result = convert_to_rubles(transaction)
        self.assertIsNone(result)
