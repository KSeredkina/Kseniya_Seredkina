""""""""""
1.	Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
a.	до минуты: <s> сек;
b.	до часа: <m> мин <s> сек;
c.	до суток: <h> час <m> мин <s> сек;
d.	* в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""""""""""

SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3600
SECONDS_IN_DAY = 86400

duration = int(input("Введите время в секундах для перевода: "))
days = duration // SECONDS_IN_DAY
hours = (duration - days * SECONDS_IN_DAY) // SECONDS_IN_HOUR
minutes = (duration - days * SECONDS_IN_DAY - hours * SECONDS_IN_HOUR) // SECONDS_IN_MINUTE
seconds = duration - days * SECONDS_IN_DAY - hours * SECONDS_IN_HOUR - minutes * SECONDS_IN_MINUTE

print(("{} дн ".format(days) if days > 0 else "") + ("{} час ".format(hours) if hours > 0 else "") + ("{} мин ".format(
    minutes) if minutes > 0 else "") + ("{} сек ".format(seconds) if seconds > 0 else ""))

# альтернативная реализация (список, кортеж и цикл)

seconds_in_time = (
    ('дн', 86400),
    ('час', 3600),
    ('мин', 60),
    ('сек', 1)
)
result_convert = []

for value, seconds_num in seconds_in_time:
    result = duration // seconds_num
    if result:
        duration -= result * seconds_num
        result_convert.append("{} {}".format(result, value))

print(result_convert)
