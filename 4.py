"""
Реализуйте базовый класс Car:
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.

"""


class Car:
    def __init__(self, name, speed, color, is_police=False):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехала'

    def stop(self):
        return f'Машина {self.name} остановилась'

    def turn(self, direction):
        return f'Машина {self.name} повернула {direction}'

    def show_speed(self):
        return f'Скорость машины {self.name} составляет {self.speed} км в час'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Скорость превышена. Текущая скорость {self.speed} км в час'
        else:
            return f'Скорость в допустимых значениях'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Скорость превышена. Текущая скорость {self.speed} км в час'
        else:
            return 'Скорость в допустимых значениях'


class PoliceCar(Car):
    pass


town = TownCar('BMW', 70, 'синий', False)
print(
    '\n' + f'Информация о первой машине: {town.go()}, {town.show_speed()}, {town.turn("направо")}, {town.turn("налево")}, '
    f'{town.stop()}')

sport = SportCar('Taycan Turbo S', 200, 'красный', False)
print('\n' + f'Информация о второй машине: {sport.go()}, {sport.show_speed()}, {sport.turn("налево")}, {sport.stop()}')

work = WorkCar('Газель', 40, 'белая', False)
print('\n' + f'Информация о третьей машине: {work.go()}, {work.show_speed()}, {work.turn("направо")}, {work.stop()}')

police = PoliceCar('Kia Rio', 100, 'серый', True)
print('\n' + f'Информация о четвертой машине: {police.go()}, {police.show_speed()}, {police.turn("налево")}, {police.stop()}')
