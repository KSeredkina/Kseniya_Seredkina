"""""""""
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
num_translate("one")
"один"
num_translate("eight")
"восемь"

Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для перевода: 
какой тип данных выбрать, в теле функции или снаружи.

*Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными, начинающимися 
с заглавной буквы — результат тоже должен быть с заглавной. Например:
num_translate_adv("One")
"Один"
num_translate_adv("two")
"два"


"""""""""""
NUMBERS_TRANSLATED_DICT = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate(english_numeral):
    """
    Translation of numerals from English to Russian from a given dictionary (from 1 to 10).
    Lowercase only.
    :param english_numeral: numeral for translation in English
    :return: translated numeral in Russian
    """
    return NUMBERS_TRANSLATED_DICT.get(english_numeral)


def num_translate_adv(english_numeral_with_register):
    """
    Translation of numerals from English to Russian from a given dictionary (from 1 to 10).
    In uppercase and lowercase.
    :param english_numeral_with_register: numeral for translation in English
    :return: translated numeral in Russian
    """
    if english_numeral_with_register.islower():
        return NUMBERS_TRANSLATED_DICT.get(english_numeral_with_register)
    else:
        return (NUMBERS_TRANSLATED_DICT.get(english_numeral_with_register.lower())).capitalize()


print(num_translate('eleven'))
print(num_translate('ten'))
print(num_translate_adv('two'))
print(num_translate_adv('Seven'))
