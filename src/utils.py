import json


def load_transactions(file_path):
    ''' Функция, которая принимает на вход путь до JSON-файла и возвращает список
         словарей с данными о финансовых транзакциях. Если файл пустой, содержит не список
          или не найден, функция возвращает пустой список. '''
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return []


# Пример использования функции
transactions = load_transactions('../data/operations.json')
print(transactions)
