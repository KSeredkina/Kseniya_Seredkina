"""
Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное число».
Реализовать перегрузку методов сложения и умножения комплексных чисел.
Проверить работу проекта. Для этого создать экземпляры класса (комплексные числа), выполнить сложение и
умножение созданных экземпляров. Проверить корректность полученного результата.

"""


class ComplexNumber:
    def __init__(self, re_complex_num, im_complex_num):
        self.re_complex_num = re_complex_num
        self.im_complex_num = im_complex_num
        self.complex_num = 're_complex_num + im_complex_num * i'

    def __add__(self, other):
        print(f'Сумма 2х комплексных чисел равна')
        return f'complex_num = {self.re_complex_num + other.re_complex_num} + ' \
               f'{self.im_complex_num + other.im_complex_num} * i '

    def __mul__(self, other):
        print(f'Произведение 2х комплексных чисел равно')
        return f'complex_num = ' \
               f'{(self.re_complex_num * other.re_complex_num)-(self.im_complex_num * other.im_complex_num)} ' \
               f'+ {(self.re_complex_num * other.im_complex_num) + (other.re_complex_num * self.im_complex_num)} * i '

    def __str__(self):
        return f'complex_num = {self.re_complex_num} + {self.im_complex_num} * i'


complex_num_1 = ComplexNumber(5, -2)
complex_num_2 = ComplexNumber(1, 8)
print(complex_num_1)
print(complex_num_1 + complex_num_2)
print(complex_num_1 * complex_num_2)
