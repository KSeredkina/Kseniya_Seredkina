"""
1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить
список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
"""
import requests

response = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
text_response = response.text
logs_truples = []
with open('logs_nginx.txt', 'w', encoding='utf-8') as f:
    f.write(text_response)

with open('logs_nginx.txt', 'r', encoding='utf-8') as f:
    for line in f:
        list_line = line.split()
        remote_addr = list_line[0]
        request_type = list_line[5][1:]
        requested_resource = list_line[6]
        logs_truples.append((remote_addr, request_type, requested_resource))

for log_line in logs_truples:
    print(log_line)
