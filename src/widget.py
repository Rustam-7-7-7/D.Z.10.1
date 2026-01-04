import datetime
from typing import Union

from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(type_and_number: Union[str]) -> Union[str]:
    '''функция, которая умеет обрабатывать информацию как о картах, так и о счетах.'''

    text_result = ""
    digit_result = ""
    digit_count = 0
    for el in type_and_number:
        if el.isdigit():
            digit_result += el
            digit_count += 1
        else:
            text_result += el
    if digit_count > 16:
        return f"{text_result}{get_mask_account(digit_result)}"
    else:
        return f"{text_result}{get_mask_card_number(digit_result)}"


def get_date(user_date: Union[str]) -> Union[str]:
    '''Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407" и
       возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024").'''

    if user_date == '':
        return ("Введено пустое значение.")

    date_format = datetime.datetime.strptime(user_date, "%Y-%m-%dT%H:%M:%S.%f")
    new_date = date_format.strftime("%d.%m.%Y")

    return new_date
