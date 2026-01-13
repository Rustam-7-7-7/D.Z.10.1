import json


def load_transactions(file_path, success=True):
    ''' Функция, которая принимает на вход путь до JSON-файла и возвращает список
         словарей с данными о финансовых транзакциях. Если файл пустой, содержит не список
          или не найден, функция возвращает пустой список. '''

    if success:
        logger.info('Функция выполнена успешно.')
    else:
        logger.error('В функции произошла ошибка.')

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return []


# Пример использования функции
# transactions = load_transactions('../data/operations.json')
# print(transactions)


# Логирование
import logging

logger = logging.getLogger('utils')

logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('../logs/utils.log', mode='w', encoding="utf--8")

file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)

# Пример использования логера
transactions = load_transactions('../data/operations.json', success=True)
print(transactions)

transactions = load_transactions('../data/operations.json', success=False)
print(transactions)
