"""
3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка — один пользователь,
разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и
формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл.
Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи
"""
import json
import sys

dictionary_person_hobby: dict[str:list[str]] = {
}
list_hobbies = []
with open('users.csv', 'r', encoding='utf-8') as f:
    for person_name in f:
        # person_name.replace(',', '.')
        # print(person_name)
        if dictionary_person_hobby.get(person_name) is None:
            dictionary_person_hobby.setdefault(person_name.replace(',', ' ').replace('\n', ''), [])


with open('hobby.csv', 'r', encoding='utf-8') as f:
    for hobby in f:
        list_hobbies.append(hobby.replace('\n', '').split(','))

count_hobby = 0
for key in dictionary_person_hobby:
    if len(list_hobbies) <= len(dictionary_person_hobby):
        if count_hobby < len(list_hobbies):
            dictionary_person_hobby[key] += list_hobbies[count_hobby]
            count_hobby += 1
        else:
            dictionary_person_hobby[key] += ['None']
    else:
        sys.exit(1)

with open('users_hobbies.json', 'w', encoding='utf-8') as f:
    json.dump(dictionary_person_hobby, f)

with open('users_hobbies.json', 'r', encoding='utf-8') as f:
    dict_reload = json.load(f)

# print(dictionary_person_hobby)
# print(dict_reload)
