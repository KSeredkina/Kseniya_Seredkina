"""""""""
5. Создать вручную список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]

a. Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп 
(например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, 
получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).  
b. Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после 
сортировки остался тот же).
c. Создать новый список, содержащий те же цены, но отсортированные по убыванию.
d. Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
"""""""""
import random

# генерация случайных вещественных чисел в массив длиной 20, округленных до 2х знаков после запятой
prices = [random.choice([round(random.uniform(0.2, 25.5), 2)]) for count in range(20)]
# prices = [23.54, 23.1, 23.0, 1.95, 2.0, 299.98, 76.08]

# реализация задания а.

for price in prices:
    price = str(price)
    integer_part_price = int(price[:price.index('.')])
    float_part_price = int(price[price.index('.') + 1:])
    print(f'{integer_part_price:02d} руб {float_part_price:02d} коп')

# реализация задания b.
print(f'Исходный список: {prices}. Ячейка в памяти: {id(prices)}')
prices.sort()
print(f'Отсортированный список по возрастанию: {prices}. Ячейка в памяти: {id(prices)}')

# реализация задания c.
prices_descending = sorted(prices, reverse=True)
print(f'Отсортированный список по убыванию: {prices_descending}. Ячейка в памяти: {id(prices_descending)}')

# реализация задания d.
the_most_expensive_prices = prices[:]
the_most_expensive_prices.sort(reverse=True)
print(f'Цены пяти самых дорогих товаров: {the_most_expensive_prices[:5]}')

# реализация алгоритма сортировки без списка и использования метода sort()
for price_index in range(len(prices)):
    lowest_price_index = price_index
    for _price_index in range(price_index + 1, len(prices)):
        if prices[_price_index] < prices[lowest_price_index]:
            lowest_price_index = _price_index
    prices[price_index], prices[lowest_price_index] = prices[lowest_price_index], prices[price_index]
# print(f'Отсортированный список: {prices}. Ссылка на отсортированный объект в памяти: {id(prices)}')
