"""
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
"""

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

unique_numbers = set()
_repeat_numbers = set()
for num in src:
    if num not in _repeat_numbers:
        unique_numbers.add(num)
    else:
        unique_numbers.discard(num)
    _repeat_numbers.add(num)

print(f'Множество неповторяющихся чисел, без сохранения порядка. {unique_numbers}')

unique_numbers_with_ord = [num for num in src if num in unique_numbers]
print(f'Список неповторяющихся чисел, с сохранением первоначального порядка. {unique_numbers_with_ord}')
