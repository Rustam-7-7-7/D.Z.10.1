from datetime import datetime


def filter_by_state(data, state='EXECUTED'):
    '''Функция, которая принимает список словарей и опционально значение для ключа 
       state (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, 
       содержащий только те словари, у которых ключ state соответствует указанному значению.'''

    return [item for item in data if item.get('state') == state]


def sort_by_date(data, reverse=True):
    '''Функция, которая принимает список словарей и необязательный параметр, задающий
       порядок сортировки(по умолчанию — убывание).Функция должна возвращать новый список, 
       отсортированный по дате(date).'''

    return sorted(data, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=reverse)
