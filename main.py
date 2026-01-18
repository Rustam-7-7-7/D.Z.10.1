def main():
    ''' Функция, которая отвечает за основную логику проекта с пользователем и связывает
         функциональности между собой. Функция предоставляет пользовательский интерфейс в
          соответствии с условиями задания. '''

    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n'
          'Выберите необходимый пункт меню:\n'
          '1. Получить информацию о транзакциях из JSON-файла\n'
          '2. Получить информацию о транзакциях из CSV-файла\n'
          '3. Получить информацию о транзакциях из XLSX-файла\n')

    valid_menu_numbers = ["1", "2", "3"]

    while True:
        menu_number = input(f'Введите соответствующую цифру (1 или 2 или 3): ')
        if menu_number in valid_menu_numbers:

            break
        else:
            print("Неправильный ввод, попробуйте снова.")

    if menu_number == '1':
        print('Для обработки выбран JSON-файл.')
        from src.utils import load_transactions
        transactions = load_transactions('data/operations.json')


    elif menu_number == '2':
        print('Для обработки выбран CSV-файл.')
        from src.file_readers import read_financial_operations_from_csv
        file_path = 'data/transactions.csv'
        transactions = read_financial_operations_from_csv(file_path)


    elif menu_number == '3':
        print('Для обработки выбран XLSX-файл.')
        from src.file_readers import read_financial_operations_from_excel
        file_path = 'data/transactions_excel.xlsx'
        transactions = read_financial_operations_from_excel(file_path)

    valid_menu_status = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        menu_status = input(f'Введите статус, по которому необходимо выполнить фильтрацию.\n'
                            'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: ').upper()
        if menu_status in valid_menu_status:
            print(f'Операции отфильтрованы по статусу "{menu_status}"')
            break
        else:
            print(f'Статус операции "{menu_status}" недоступен.')

    from src.processing import filter_by_state
    state = menu_status
    transactions = filter_by_state(transactions, state)

    valid_menu_date = ["ДА", "НЕТ"]

    while True:
        menu_date = input('Отсортировать операции по дате? Да/Нет: ').upper()
        if menu_date in valid_menu_date:

            break
        else:
            print(f'Статус сортировки "{menu_date}" недоступен.')

    if menu_date == 'ДА':
        from src.processing import sort_by_date

        valid_menu_reverse = ["по возрастанию", "по убыванию"]

        while True:
            menu_reverse = input('Отсортировать по возрастанию или по убыванию?: ').lower()
            if menu_reverse in valid_menu_reverse:

                break
            else:
                print(f'Статус сортировки "{menu_reverse}" недоступен.')

        if menu_reverse == "по возрастанию":
            transactions = sort_by_date(transactions, reverse=False)

        if menu_reverse == "по убыванию":
            transactions = sort_by_date(transactions, reverse=True)

    valid_menu_rub = ["ДА", "НЕТ"]

    while True:
        menu_rub = input('Выводить только рублевые транзакции? Да/Нет: ').upper()
        if menu_rub in valid_menu_rub:

            break
        else:
            print(f'Статус сортировки "{menu_rub}" недоступен.')

    if menu_rub == 'ДА':
        from src.generators import filter_by_currency
        transactions = filter_by_currency(transactions, "RUB")

    valid_menu_search = ["ДА", "НЕТ"]

    while True:
        menu_search = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ').upper()
        if menu_search in valid_menu_search:

            break
        else:
            print(f'Статус фильтрования "{menu_search}" недоступен.')

    if menu_search == 'ДА':
        from src.process_bank import process_bank_search
        search_word = input(f'Введите слово: ')
        transactions = process_bank_search(transactions, search=search_word)

    if transactions == []:
        return print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации. '
                     'Работа программы окончена.')

    print('Распечатываю итоговый список транзакций...')

    print(f"Всего банковских операций в выборке: {len(transactions)}")
    print()

    from src.widget import mask_account_card

    for transaction in transactions:
        if 'from' in transaction:
            transaction['from'] = mask_account_card(transaction['from'])
        if 'to' in transaction:
            transaction['to'] = mask_account_card(transaction['to'])

    for transaction in transactions:
        date = transaction['date'][:10]
        formatted_date = f"{date[8:10]}.{date[5:7]}.{date[:4]}"
        description = transaction['description']

        from_account = transaction.get('from', 'неизвестно')
        to_account = transaction.get('to', 'неизвестно')

        amount = transaction['operationAmount']['amount']
        currency = transaction['operationAmount']['currency']['name']

        print(f"{formatted_date} {description}")
        print(f"{from_account} -> {to_account}")
        print(f"Сумма: {amount} {currency}\n")
    return print('Работа программы окончена.')


main()
