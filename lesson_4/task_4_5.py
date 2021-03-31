"""
*(вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:

python task_4_5.py USD
75.18, 2020-09-05
"""
from datetime import datetime
from xml.etree import ElementTree

import requests


def currency_rates_parsing(argv):
    """
    Function use variable from interpreter. Parsing api from web with using library ElementTree.
    Return price of input currency and date of rate.
    :param argv: Variables from interpreter
    :return: Price of currency and date of rate
    """
    program, *args = argv
    value_currency = None
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    tree_request = ElementTree.fromstring(response.content)
    date_rate = tree_request.get('Date')
    date_rate = datetime.strptime(date_rate, "%d.%m.%Y").date()
    date_rate.isoformat()
    if len(args) == 1:
        for tag_currency in tree_request.findall('Valute'):
            if args[0].upper() == tag_currency.find('CharCode').text:
                value_currency = float(tag_currency.find('Value').text.replace(',', '.'))
        print(f'Дата курса валюты: {date_rate}. Стоимость введенной валюты: {value_currency}')
    else:
        print('Нужен один аргумент в виде кода валюты')
    return 0


def main(argv):
    program, *args = argv
    result = sum(map(int, args))
    print(f'результат: {result}')

    return 0


if __name__ == '__main__':
    import sys

    exit(currency_rates_parsing(sys.argv))
