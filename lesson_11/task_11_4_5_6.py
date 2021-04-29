"""
Начать работу над проектом «Склад оргтехники».
Cоздать класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведённых типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

Продолжить работу над предыдущим заданием.
Разработать методы, которые отвечают за приём оргтехники на склад и передачу в определённое
подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру (например, словарь).

Продолжить работу над предыдущим заданием.
Реализовать механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

"""


class NotFoundTechniqueType(Exception):
    def __init__(self, txt):
        self.txt = txt


class InvalidSkuNumber(Exception):
    def __init__(self, message):
        self.message = message


class Storage:
    __office_technique_collection = {}
    __structure_transfered_technique = {}

    def receive_technique(self, technique_type: str, technique_parameter: dict):
        try:
            if not self.__office_technique_collection.get(technique_type):
                self.__office_technique_collection[technique_type] = [technique_parameter]
            else:
                self.__office_technique_collection[technique_type].append(technique_parameter)
        except NotFoundTechniqueType as error:
            print(error.txt)

    def transfer_technique_to_structure(self, structure: str, technique_type: str, technique_sku_number: str):
        try:
            if not self.__office_technique_collection.get(technique_type):
                raise NotFoundTechniqueType(f'Оборудование {technique_type} не учитывается на складе')

            if not self.__validate_sku(technique_sku_number, technique_type):
                raise InvalidSkuNumber(
                    f'Артикул {technique_sku_number} не найден в заданном типе оборудования {technique_type}')

            if not self.__structure_transfered_technique.get(structure):
                self.__structure_transfered_technique.setdefault(structure, {technique_type: [technique_sku_number]})
            else:
                self.__structure_transfered_technique[structure][technique_type].append(technique_sku_number)

            for index in range(0, len(self.__office_technique_collection.get(technique_type))):
                if self.__office_technique_collection.get(technique_type)[index].get('sku') == technique_sku_number:
                    index_del = index
            print(self.__office_technique_collection.get(technique_type)[index_del])
            self.__office_technique_collection.get(technique_type).pop(index)

        except NotFoundTechniqueType as error:
            print(error.txt)
        except InvalidSkuNumber as sku_error:
            print(sku_error.message)
        except IndexError as e:
            print(e)

    def __validate_sku(self, technique_sku_number: str, technique_type: str):
        for item in self.__office_technique_collection[technique_type]:
            if item['sku'] == technique_sku_number:
                return True
            else:
                return False

    def get_full_technique(self):
        result = {}
        for technique_type, technique_list in self.__office_technique_collection.items():
            result[technique_type] = len(technique_list)
        return result


class OfficeTechnique:
    def __init__(self, technique_type: str, title: str, sku: str):
        self.technique_type = technique_type
        self.title = title
        self.sku = sku


class Scan(OfficeTechnique):
    TECHNIQUE_TYPE = 'scan'

    def __init__(self, title, sku, dpi: int):
        super().__init__(self.TECHNIQUE_TYPE, title, sku)
        self.dpi = dpi


class Xerox(OfficeTechnique):
    TECHNIQUE_TYPE = 'xerox'

    def __init__(self, title, sku, is_color):
        super().__init__(self.TECHNIQUE_TYPE, title, sku)
        self.is_color = is_color


class Printer(OfficeTechnique):
    TECHNIQUE_TYPE = 'printer'

    def __init__(self, title, sku, is_color: bool):
        super().__init__(self.TECHNIQUE_TYPE, title, sku)
        self.is_color = is_color


storage = Storage()
scan_1 = Scan(title="hp", dpi=123, sku='h-11-22-32')
scan_2 = Scan(title="canon", dpi=321, sku='c-66-77-82')
xerox_1 = Xerox(title='xerox', is_color=True, sku='xe-11-22')
printer_1 = Printer(title='epson', is_color=False, sku='pr-123')
printer_2 = Printer(title='canon', is_color=True, sku='pr-456')

storage.receive_technique(Printer.TECHNIQUE_TYPE, printer_1.__dict__)
storage.receive_technique(Printer.TECHNIQUE_TYPE, printer_2.__dict__)
storage.receive_technique(Scan.TECHNIQUE_TYPE, scan_1.__dict__)
storage.receive_technique(Scan.TECHNIQUE_TYPE, scan_2.__dict__)
storage.receive_technique(Xerox.TECHNIQUE_TYPE, xerox_1.__dict__)
print(storage._Storage__office_technique_collection)
storage.transfer_technique_to_structure('отдел продаж', 'printer', 'pr-123')
print(storage._Storage__structure_transfered_technique)
print(storage._Storage__office_technique_collection)
