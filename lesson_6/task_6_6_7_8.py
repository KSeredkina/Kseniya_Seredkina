"""
6. Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два скрипта
с интерфейсом командной строки: для записи данных и для вывода на экран записанных данных. При записи передавать
из командной строки значение суммы продаж. Для чтения данных реализовать в командной строке следующую логику:
просто запуск скрипта — выводить все записи;
запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер, равный второму
числу, включительно.

7. Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1. Примеры запуска скриптов:

python add_sale.py 5978,5
python add_sale.py 8914,3
python add_sale.py 7879,1
python add_sale.py 1573,7
python show_sales.py
5978,5
8914,3
7879,1
1573,7
python show_sales.py 3
7879,1
1573,7
python show_sales.py 1 3
5978,5
8914,3
7879,1
7. * (вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта: передаём ему номер записи
и новое значение. При этом файл не должен читаться целиком — обязательное требование.
Предусмотреть ситуацию, когда пользователь вводит номер записи, которой не существует.
"""
file_name = 'bakery.csv'


def add_sale(argv):
    program, *args = argv
    if args is not None:
        with open(file_name, 'a', encoding='utf-8') as f:
            for sale in args:
                f.write(sale + '\n')
            return 0


def show_sale(argv):
    program, *args = argv
    with open(file_name, 'r', encoding='utf-8') as f:
        if len(args) == 0:
            for sale in f:
                print(sale.rstrip())
        elif len(args) == 1:
            index_sale = list(map(int, args))
            for idx, sale in enumerate(f):
                if idx >= index_sale[0] - 1:
                    print(sale.rstrip())
        elif len(args) == 2:
            index_sale = list(map(int, args))
            for idx, sale in enumerate(f):
                if index_sale[0] - 1 <= idx <= index_sale[1] - 1:
                    print(sale.rstrip())
    return 0


def edit_sale(argv):
    program, *args = argv
    index_sale = int(args[0])
    edit_sale = args[1]

    with open(file_name, 'r', encoding='utf-8') as f:
         sales_list = f.readlines()

    if index_sale < len(sales_list):
         sales_list[index_sale - 1] = edit_sale + '\n'
    else:
        print('Цены с таким порядковым номером нет в файле')

    with open(file_name, 'w', encoding='utf-8') as file_new:
         file_new.writelines(sales_list)

    # with open(file_name, 'r', encoding='utf-8') as f:
    #     pos = 0
    #     index_sale = int(args[0])
    #     # index_sale = list(map(int, args))
    #     for idx, sale in enumerate(f):
    #         if idx < index_sale - 1:
    #             pos += len(sale) + 1
    # with open(file_name, 'r+', encoding='utf-8') as f:
    #     f.seek(pos)
    #     f.writelines(args[1])

    return 0


if __name__ == '__main__':
    import sys

    # exit(add_sale(sys.argv))
    exit(edit_sale(sys.argv))
    # exit(show_sale(sys.argv))
