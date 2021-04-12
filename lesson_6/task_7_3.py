"""
Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
   |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html


Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
(они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача,
которая решена, например, во фреймворке django.

"""
import os
import shutil
from collections import defaultdict
from os.path import relpath

root_path = r'C:\Users\KSeredkina\PycharmProjects\Kseniya_Seredkina\lesson_6\my_project'
subfolder = 'templates'
try:
    for folder_path, dirs, files in os.walk(root_path):
        subfolder_path = os.path.join(root_path, subfolder)
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)
        for file in files:
            extension_file = file.rsplit('.', maxsplit=1)[-1].lower()
            folder_name = os.path.basename(folder_path)
            new_folder_path = os.path.join(subfolder_path, folder_name)
            if extension_file == 'html' and not os.path.exists(new_folder_path):
                shutil.move(folder_path, new_folder_path)
except (FileNotFoundError, EOFError) as e:
    print(f'Text error: {e}')


        # current_file_path = os.path.join(folder_path, file)
        # new_file_path = os.path.join(root_path, file)
        # rename_count = 0
        # if extension_file != 'html' and os.path.exists(new_file_path) and os.path.basename(
        #         folder_path) != os.path.basename(root_path) and rename_count < 1:
        #     file_new = file.split('.')[0] + '_' + os.path.basename(folder_path) + '.' + file.split('.')[1]
        #     current_file_path_rename = os.path.join(folder_path, file_new)
        #     new_file_path_rename = os.path.join(root_path, file_new)
        #     shutil.move(current_file_path, current_file_path_rename)
        #     shutil.move(current_file_path_rename, new_file_path_rename)
        #     rename_count +=1
        # elif extension_file != 'html' and not os.path.exists(new_file_path):
        #     shutil.move(current_file_path, new_file_path)

            # current_file_path_rename = os.path.join(folder_path, file_new)
            # new_file_path_rename = os.path.join(root_path, file_new)
            # shutil.move(current_file_path_rename, new_file_path_rename)
            # print(current_file_path)
            # print(new_file_path)
        # elif extension_file != 'html' and not os.path.exists(new_file_path):
        # shutil.move(current_file_path, new_file_path)    #current_file_path = os.path.join(folder_path, file_new)
        # new_file_path = os.path.join(root_path, file_new)
        # shutil.move(current_file_path, new_file_path)
        # new_file_path += '_' + os.path.basename(folder_path)
        # shutil.move(current_file_path, new_file_path)
        # shutil.move(file, os.path.join(root_path, file))
        # print(type(os.path.basename(folder_path)))
        # print(file)
        # print(os.path.exists(file))
