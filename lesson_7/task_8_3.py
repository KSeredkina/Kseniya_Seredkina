"""
Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...

@type_logger
def calc_cube(x):
   return x ** 3

a = calc_cube(5)
5: <class 'int'>

Примечание: если аргументов несколько - выводить данные о каждом через запятую; +
можете ли вы вывести тип значения функции?+
Сможете ли решить задачу для именованных аргументов? +
Сможете ли вы замаскировать работу декоратора?
Сможете ли вывести имя функции, например, в виде:
a = calc_cube(5)
calc_cube(5: <class 'int'>) +
"""
from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        list_arg_type = []
        for argument in args:
            if argument:
                list_arg_type.append(f'{argument}:{type(argument)}')
        for argument_value in kwargs.values():
            if argument_value:
                list_arg_type.append(f'{argument_value}: {type(argument_value)}')
        result_func = func(*args, **kwargs)
        return print(f'{func.__name__}({str(list_arg_type)[1:-1]}), result type:{type(result_func)}')

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


@type_logger
def print_results(*args, **kwargs):
    return "тестовые данные"


result_func_1 = calc_cube(3)
result_func_2 = print_results(4, 5, f='1324')
