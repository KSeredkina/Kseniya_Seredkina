"""
Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя
и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.
 Пример:
email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru


Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; имеет ли смысл в
данном случае использовать функцию re.compile()?

"""
import re


def email_parse(email):
    dict_parsed_email = {}
    msg = f'wrong email: {email}'
    # regex = r'[^@]+@[^@]+\.[^@]+'
    regex = r'^([a-z0-9]){1}(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,6}$'
    if re.match(regex, email):
        parsed_email = re.split(r'@', email)
        dict_parsed_email['user_name'] = parsed_email[0]
        dict_parsed_email['domain'] = parsed_email[1]
        print(dict_parsed_email)
    else:
        raise ValueError(msg)


# email_parse('someone@geekbrain.sru')
email_parse('1some.one@geek-brain.sru')

# RE_EMAIL = re.compile(r'[^@]+@[^@]+\.[^@]+')
#
# for email in ['someone@geekbrains.ru', '1111111@gggg.ins.ru']:
#     assert RE_EMAIL.match(email), f"wrong date {email}"
