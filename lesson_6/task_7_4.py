"""
Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
а значения — общее количество файлов (в том числе и в подпапках),
размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }

Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat
"""
import os

import django

root_dir = django.__path__[0]
print(root_dir)
dict_size_count_files = {}
short_number = 10
for folder_path, dirs, files in os.walk(root_dir):
    key_num = 1
    for file in files:
        file_path = os.path.join(folder_path, file)
        key_list = [short_number ** nums for nums in range(0, 10)]
        if key_num < len(key_list):
            if key_list[key_num] < os.stat(file_path).st_size <= key_list[key_num + 1]:
                if dict_size_count_files.get(key_list[key_num + 1]) is None:
                    dict_size_count_files.setdefault(key_list[key_num + 1], 1)
                else:
                    dict_size_count_files[key_list[key_num + 1]] += 1
                key_num += 1
            else:
                key_num += 1

for size_file, count_file in sorted(dict_size_count_files.items()):
    print(f'{size_file}: {count_file}')
