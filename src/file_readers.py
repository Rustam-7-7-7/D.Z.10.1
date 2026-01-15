import csv


def read_financial_operations_from_csv(file_path):
    ''' Функция для считывания финансовых операций из CSV-файла. '''

    transactions = []

    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'state', 'date', 'amount', 'currency_name', 'currency_code', 'from', 'to', 'description']

        csvreader = csv.DictReader(csvfile, fieldnames=fieldnames, delimiter=';')

        next(csvreader, None)

        for row in csvreader:
            transactions.append(row)

    return transactions


# Пример использования
file_path = '../data/transactions.csv'
transactions = read_financial_operations_from_csv(file_path)

for transaction in transactions:
    print(transaction)

######################################################################
import pandas as pd


def read_financial_operations_from_excel(file_path):
    ''' Функция для считывания финансовых операций из Excel-файла. '''

    df = pd.read_excel(file_path)

    transactions = df.to_dict(orient='records')

    return transactions


# Пример использования
file_path = '../data/transactions_excel.xlsx'
transactions = read_financial_operations_from_excel(file_path)

for transaction in transactions:
    print(transaction)
