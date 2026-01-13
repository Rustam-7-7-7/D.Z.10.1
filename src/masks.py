# Домашнее задание № 13.1
#############################################################################


def get_mask_card_number(card_number: int, success=True) -> str:
    '''Функция, которая принимает на вход номер карты и возвращает ее маску.'''

    if success:
        logger.info('Функция выполнена успешно.')
    else:
        logger.error('В функции произошла ошибка.')

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: int, success=True) -> str:
    '''Функция, которая принимает на вход номер счета и возвращает его маску.'''

    if success:
        logger.info('Функция выполнена успешно.')
    else:
        logger.error('В функции произошла ошибка.')

    return f"**{account_number[-4:]}"


# Логирование
import logging

logger = logging.getLogger('masks')

logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('../logs/masks.log', mode='w', encoding="utf--8")

file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)

# Пример использования логера
# card_number = input(f'Введите номер карты: ')
#
# print(get_mask_card_number(card_number, success=True))
#
# print(get_mask_card_number(card_number, success=False))

#############################################################################
