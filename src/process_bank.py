import re


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    ''' Функция, которая будет принимать список словарей с данными о банковских операциях и строку
         поиска, а возвращать список словарей, у которых в описании есть данная строка. '''

    result = []
    for transaction in data:
        description = transaction.get('description', '')
        if re.search(search, description, re.IGNORECASE):
            result.append(transaction)
    return result


###----------------------------------------------------------
from collections import Counter


def process_bank_operations(data: list[dict], categories: list) -> dict:
    ''' Функция, которая будет принимать список словарей с данными о банковских операциях и список
         категорий операций, а возвращать словарь, в котором ключи — это названия категорий, а
          значения — это количество операций в каждой категории. '''

    category_counter = Counter()

    categories_lower = [category.lower() for category in categories]

    for transaction in data:

        description = transaction.get('description', '').lower()

        for category in categories_lower:
            if category in description:
                category_counter[category] += 1

    return dict(category_counter)
