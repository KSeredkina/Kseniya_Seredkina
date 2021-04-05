"""
Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]

Подсказка: использовать возможности python, изученные на уроке. Подумайте, как можно сделать оптимизацию кода по памяти,
 по скорости.
"""
import sys
from time import perf_counter

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 678]

start_1 = perf_counter()

result = []
for index in range(1, len(src)):
    if src[index] > src[index - 1]:
        result.append(src[index])

print(f'Вариант 1. Реализация через списки {type(result)}. Результат: {result}.')
print(f'Время исполнения: {perf_counter() - start_1}. Занимаемое место в памяти: {sys.getsizeof(result)}')

# Синтаксический сахар. List Comprehensions
start_2 = perf_counter()
res = [src[indx] for indx in range(1, len(src)) if src[indx] > src[indx - 1]]
print(f'Вариант 2. Реализация с использование list comprehensions {type(res)}.')
print('Результат: ', res)
print(f'Время исполнения: {perf_counter() - start_2}. Занимаемое место в памяти: {sys.getsizeof(res)}')

start_3 = perf_counter()
result_gen = (src[indx] for indx in range(1, len(src)) if src[indx] > src[indx - 1])
print(f'Вариант 3. Реализация через генератор {type(result_gen)}.')
print('Результат: ', *result_gen)
print(f'Время исполнения: {perf_counter() - start_3}. Занимаемое место в памяти: {sys.getsizeof(result_gen)}')
