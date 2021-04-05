"""
Есть два списка:
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
('Иван', '9А')
('Анастасия', '7В')
...

Количество генерируемых кортежей не должно быть больше длины списка tutors.
Если в списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде:
 (<tutor>, None), например:
('Станислав', None)

Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
Подумать, в каких ситуациях генератор даст эффект.
"""

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В'
]

gen_pairs_tutor_klass = (pair for pair in zip(tutors, klasses))


# print(next(gen_pairs_tutor_klass), next(gen_pairs_tutor_klass), next(gen_pairs_tutor_klass),
#      next(gen_pairs_tutor_klass), next(gen_pairs_tutor_klass),
#      next(gen_pairs_tutor_klass), next(gen_pairs_tutor_klass), sep=', ')

def generate_pairs_of_lists(list_1, list_2):
    number_pair = 0
    while number_pair < len(list_1):
        if number_pair > len(list_2) - 1:
            yield list_1[number_pair], None
        else:
            yield list_1[number_pair], list_2[number_pair]
        number_pair += 1


print(*generate_pairs_of_lists(tutors, klasses))
