"""
* (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
размер которых превышает объем ОЗУ компьютера.
"""
dict_ip_counts = {}

with open('logs_nginx.txt', 'r', encoding='utf-8') as f:
    for line in f:
        ip = line[:line.index(' ')]
        if dict_ip_counts.get(ip) is None:
            dict_ip_counts.setdefault(ip, 1)
        else:
            dict_ip_counts[ip] += 1

max_count = max(dict_ip_counts.values())
ip_spam = None
for ip, count in dict_ip_counts.items():
    if count == max_count:
        ip_spam = ip

print(f'Спамер: {ip_spam}, количество запросов: {max_count}')
