"""""""""
Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, 
в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. 
Например:
thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"], 
    "М": ["Мария"], "П": ["Петр"]
}

Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам? 
Можно ли использовать словарь в этом случае?

*(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «
Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные 
по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
    }, 
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"], 
        "А": ["Анна Савельева"]
    }
}
"""""""""


def thesaurus(*args):
    """
    Grouping a dictionary by name
    :param args: names people
    :return: dictionary by name
    """
    dictionary_by_name = {}
    first_spells_list = list(map(lambda x: x[0], args))
    for first_spell in first_spells_list:
        dictionary_by_name[first_spell] = []
        for elm in args:
            if elm.startswith(first_spell):
                dictionary_by_name[first_spell].append(elm)
    return dictionary_by_name


def thesaurus_adv(*args):
    """
    Grouping a dictionary by first spell of name inside dictionary by first spell of surnames
    :param args: names and surnames people
    :return: dictionary by first spell of names inside dictionary by first spell of surnames
    """
    dictionary_by_surname_and_name: dict[str, dict: str, list[str]] = {
    }
    full_names_list = list(args)
    # print(f'Исходный список имен и фамилий {full_names_list}')
    for full_name in full_names_list:
        name = full_name[:full_name.index(' ')]
        name_first_spell = name[:1]
        surname = full_name[full_name.index(' ') + 1:]
        surname_first_spell = surname[:1]
        if dictionary_by_surname_and_name.get(surname_first_spell) is None:
            dictionary_by_surname_and_name.setdefault(surname_first_spell, {name_first_spell: [full_name]})

        else:
            if dictionary_by_surname_and_name.get(surname_first_spell).get(name_first_spell) is None:
                dictionary_by_surname_and_name.get(surname_first_spell).update({name_first_spell: [full_name]})
            else:
                dict(dictionary_by_surname_and_name.get(surname_first_spell)).get(name_first_spell).append(full_name)
    return dictionary_by_surname_and_name


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Ирландия Иванова",
                    "К А"))
