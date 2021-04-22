"""
Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.

"""
from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, title, parameter=None):
        self.title = title
        self.param = parameter

    def __str__(self):
        return f'Для пошива изделия {self.title} нужно: {self.fabric_consumption} метров ткани'

    @abstractmethod
    def fabric_consumption(self):
        pass

    @staticmethod
    def total_fabric_consumption(*args):
        result = 0
        for arg in args:
            result += arg
        return f'Общий расход ткани: {result} метров'


class Coat(Clothes):
    @property
    def fabric_consumption(self):
        return round(self.param / 6.5 + 0.5, 2)


class Costume(Clothes):
    @property
    def fabric_consumption(self):
        return round(2 * self.param + 0.3, 2)


coat = Coat('пальто', 375)
costume = Costume('костюм', 78)
print(coat)
print(costume)
print(Clothes.total_fabric_consumption(coat.fabric_consumption, costume.fabric_consumption))
