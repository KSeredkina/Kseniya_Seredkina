"""
Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);+
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;+
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна;
проверить работу метода.

Например: 20 м*5000 м*25 кг*5 см = 12500 т.

"""


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.mass_one_square_meter = 25
        self.height = 5

    def asphalt_weight(self):
        asphalt_weight = self._length * self._width * self.mass_one_square_meter * self.height / 1000
        print(f'Для покрытия всего дорожного полотна необходимо {round(asphalt_weight)} тонн асфальта')


road = Road(20, 50)
road.asphalt_weight()
