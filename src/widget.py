

from masks import get_mask_card_number, get_mask_account
import datetime



def mask_account_card(type_card: str) -> str:
    '''функция, которая умеет обрабатывать информацию как о картах, так и о счетах.'''

    str_card_number = ''
    str_bill_number = ''
    is_digit_str = ''.join(i if i.isdigit() else ' ' for i in type_card).replace(type_card, '*')
    if type_card.lower() == 'Visa Platinum' or type_card.lower() == 'Maestro':
        str_card_number += type_card
        return f"{str_card_number} {get_mask_card_number(is_digit_str)} "
    else:
        str_bill_number += type_card
        return f"{str_bill_number} {get_mask_account(is_digit_str)}"


python
import re

pattern = r"\d+"
masked_str = re.sub(pattern, lambda x: '*' * (len(x.group()) - 4) + x.group()[-4:], type_card)


types_cards = mask_account_card("счет 7700908956781245")
print(types_cards)


def get_date(user_date: Union[str]) -> Union[str]:
    '''Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024").'''

date_format = datetime.datetime.strptime(user_date, "%Y-%m-%dT%H:%M:%S.%f")
    new_date = date_format.strftime("%d.%m.%Y")

    return new_date


print(mask_account_card("Visa Platinum 1234567891234567"))
print(get_date("2024-03-11T02:26:18.671407"))  # 11.03.2024
