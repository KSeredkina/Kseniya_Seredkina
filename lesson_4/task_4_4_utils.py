"""
Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания. Создать скрипт,
в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
Убедиться, что ничего лишнего не происходит.
"""
from datetime import datetime
from xml.etree import ElementTree

import requests


def currency_rates_parsing(code_currency):
    """
    Parsing api from web with using library ElementTree. Return price of input currency and date of rate.
    :param code_currency: Code of currency that about need to get information
    :return: Price of currency and date of rate
    """
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    tree_request = ElementTree.fromstring(response.content)
    date_rate = tree_request.get('Date')
    date_rate = datetime.strptime(date_rate, "%d.%m.%Y").date()
    value_currency = None
    for tag_currency in tree_request.findall('Valute'):
        if code_currency.upper() == tag_currency.find('CharCode').text:
            value_currency = float(tag_currency.find('Value').text.replace(',', '.'))
    return {'date_rate of rate': date_rate, 'price of currency': value_currency}


if __name__ == '__main__':
    print(currency_rates_parsing('EUR'))
    print(currency_rates_parsing('Usd'))
    print(currency_rates_parsing('DOL'))
