"""
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield

Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
"""


def odd_numbers_generate(max_number):
    for number in range(1, max_number + 1):
        if number % 2 != 0:
            yield number


odd_numbers = odd_numbers_generate(15)
print(next(odd_numbers), next(odd_numbers), next(odd_numbers), next(odd_numbers), next(odd_numbers),
      next(odd_numbers), next(odd_numbers), next(odd_numbers), sep=', ')

max_number = int(input("До какого числа включительно генерировать нечетные числа?"))
odd_nums_gen = (number for number in range(1, max_number + 1) if number % 2 != 0)
print(next(odd_nums_gen), next(odd_nums_gen), next(odd_nums_gen), next(odd_nums_gen), next(odd_nums_gen),
      next(odd_nums_gen), next(odd_nums_gen), next(odd_nums_gen), sep=', ')
