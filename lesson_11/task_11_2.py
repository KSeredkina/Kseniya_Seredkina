"""
Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверить его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

"""


class OwnZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


def div():
    try:
        input_divisible = int(input('Введите делимое: '))
        input_divisor = int(input('Введите делитель: '))
        if input_divisor == 0:
            raise OwnZeroDivisionError("На ноль делить нельзя!")
        else:
            result = input_divisible / input_divisor
            return result
    except ValueError:
        return "Вы ввели не число"
    except OwnZeroDivisionError as e:
        return e


print(div())
