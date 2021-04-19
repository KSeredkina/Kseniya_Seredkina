"""
Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции
и выбрасывать исключение ValueError, если что-то не так, например:
def val_checker...
    ...

@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

a = calc_cube(5)
125
a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5


Примечание: сможете ли вы замаскировать работу декоратора?
"""
from functools import wraps


def val_checker(input_condition):
    def val_checker_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for is_arg_correct in filter(input_condition, args):
                return func(*args, **kwargs)
            else:
                for arg in args:
                    raise ValueError(f'wrong val {arg}')

        return wrapper

    return val_checker_decorator


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube.__name__)
print(calc_cube(5))
print(calc_cube(-5))
