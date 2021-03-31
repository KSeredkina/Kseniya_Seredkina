"""
Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
Рекомендация: выполнить предварительно запрос
к API в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str,
решить поставленную задачу? Функция должна возвращать результат числового типа, например float.
Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты, которого нет в ответе,
вернуть None. Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
В качестве примера выведите курсы доллара и евро.

*(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, которая передаётся
в ответе сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа, какой тип данных
лучше использовать в ответе функции?

"""
from datetime import datetime

import requests

from lesson_4 import task_4_4_utils


def currency_rates(code_currency):
    """
    Parsing api from web with using only strings. Return price of input currency and date of rate.
    :param code_currency: Code of currency that about need to get information
    :return: Price of currency and date of rate
    """
    request = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    text_request = request.text
    price_currency = None
    date_rate = None
    for text_string in text_request.split('<CharCode>'):
        if text_string.find('Date="') != -1:
            date_rate = text_string[text_string.find('Date="') + 6:text_string.find('Date="') + 16]
            date_rate = datetime.strptime(date_rate, "%d.%m.%Y").date()
        if code_currency.upper() in text_string:
            value_currency = text_string.split('<Value>')
            price_currency = float(value_currency[1][:7].replace(',', '.'))
    return {'date_currency': date_rate, 'price_currency': price_currency}


# print(currency_rates('eur'))
# print(currency_rates('DOL'))

print(task_4_4_utils.currency_rates_parsing('EUR'))
