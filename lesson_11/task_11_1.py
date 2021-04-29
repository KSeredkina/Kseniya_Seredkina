"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый — с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй — с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""
from datetime import datetime


class Date:
    date_format = '%d-%m-%Y'
    @classmethod
    def cut_date(cls, date_string):
        try:
            if Date.validate(date_string, cls.date_format):
                date_list = []
                for i in date_string.split('-'):
                    if i != '-':
                        date_list.append(int(i))
                return date_list
            else:
                raise ValueError

        except ValueError:
            return f'Некорректный формат. Должен быть DD-MM-YYYY'

    @staticmethod
    def validate(date_string, date_format):
        try:
            if date_string != datetime.strptime(date_string, date_format).strftime(date_format):
                raise ValueError
            return True
        except ValueError:
            return False

print(Date.validate('23-02-2021', Date.date_format))
print(Date.cut_date('23-02-2021'))


