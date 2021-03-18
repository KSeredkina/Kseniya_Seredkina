""""""""""
2.	Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
a.	Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859»
 будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические 
 операции!
b.	К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых 
делится нацело на 7. 
c.	* Решить задачу под пунктом b, не создавая новый список.
"""""""""""

third_degree_numbers = []
sum_numbers = 0
sum_increased_numbers = 0

for number in range(1, 1001):
    if number % 2 != 0:
        third_degree_numbers.append(number ** 3)

for number in third_degree_numbers:
    sum_digit = 0
    sum_increased_digit = 0
    _temp_num = number
    _increased_num = (number + 17)
    # поиск суммы цифр числа из списка
    while _temp_num != 0:
        sum_digit += _temp_num % 10
        _temp_num = _temp_num // 10
    # поиск суммы цифр увеличенного на 17 числа из списка
    while _increased_num != 0:
        sum_increased_digit += _increased_num % 10
        _increased_num = _increased_num // 10

    if sum_digit % 7 == 0:
        sum_numbers += number

    if sum_increased_digit % 7 == 0:
        sum_increased_numbers += (number + 17)

        # print(" ")
        # print("Число: ", number)
        # print("Сумма цифр числа равна: ", sum_digit)
print(third_degree_numbers)
print("Сумма чисел, сумма цифр которых делится нацело на 7 равна: ", sum_numbers)
# print(" ")
# print("Число увеличенное: ", number + 17)
# print("Сумма цифр увеличенного числа равна: ", sum_increased_digit)
print("Сумма увеличенных на 17 чисел, сумма цифр которых делится нацело на 7: ", sum_increased_numbers)
