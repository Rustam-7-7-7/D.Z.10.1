import json
import unittest
from unittest.mock import mock_open, patch

from src.utils import load_transactions


class TestLoadTransactions(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='[{"id": 1, "amount": 100}]')
    def test_load_valid_json(self, mock_file):
        result = load_transactions('dummy_path.json')
        self.assertEqual(result, [{"id": 1, "amount": 100}])
        mock_file.assert_called_once_with('dummy_path.json', 'r', encoding='utf-8')

    @patch('builtins.open', new_callable=mock_open, read_data='{}')
    def test_load_invalid_json_structure(self, mock_file):
        result = load_transactions('dummy_path.json')
        self.assertEqual(result, [])
        mock_file.assert_called_once_with('dummy_path.json', 'r', encoding='utf-8')

    @patch('builtins.open', new_callable=mock_open, read_data='')
    def test_load_empty_file(self, mock_file):
        result = load_transactions('dummy_path.json')
        self.assertEqual(result, [])
        mock_file.assert_called_once_with('dummy_path.json', 'r', encoding='utf-8')

    @patch('src.utils.json.load', side_effect=json.JSONDecodeError("Expecting value", "", 0))
    @patch('builtins.open', new_callable=mock_open)
    def test_load_json_decode_error(self, mock_file, mock_json_load):
        result = load_transactions('dummy_path.json')
        self.assertEqual(result, [])
        mock_file.assert_called_once_with('dummy_path.json', 'r', encoding='utf-8')

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_load_file_not_found(self, mock_file):
        result = load_transactions('non_existent_file.json')
        self.assertEqual(result, [])
        mock_file.assert_called_once_with('non_existent_file.json', 'r', encoding='utf-8')
