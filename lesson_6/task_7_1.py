"""
Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings_2
   |--mainapp
   |--adminapp
   |--authapp


Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить
конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли будет
при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
"""
import os

dict_config_dir = {'my_project': ['settings_2', 'mainapp', 'adminapp', 'authapp']}


for main_folder, list_subfolders in dict_config_dir.items():
    if list_subfolders is not None:
        for subfolder in list_subfolders:
            dir_path = os.path.join(main_folder, subfolder)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)