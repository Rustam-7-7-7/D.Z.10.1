import unittest
from unittest.mock import Mock, patch

from src.external_api import convert_to_rubles


class TestConvertToRubles(unittest.TestCase):

    @patch('src.external_api.requests.get')
    def test_convert_usd_to_rubles(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'result': 7500.0}
        mock_get.return_value = mock_response

        transaction = {'amount': 100, 'currency': 'USD'}
        result = convert_to_rubles(transaction)

        mock_get.assert_called_once()
        self.assertEqual(result, 7500.0)

    @patch('src.external_api.requests.get')
    def test_convert_eur_to_rubles(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'result': 8800.0}
        mock_get.return_value = mock_response

        transaction = {'amount': 100, 'currency': 'EUR'}
        result = convert_to_rubles(transaction)

        mock_get.assert_called_once()
        self.assertEqual(result, 8800.0)
