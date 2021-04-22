"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и пр.

"""


class Matrix:

    def __init__(self, list_elements_matrix=None):
        if list_elements_matrix is None:
            list_elements_matrix = []
        self.list_elements_matrix = list_elements_matrix

    def __str__(self):
        for row_matrix in self.list_elements_matrix:
            for element_row in row_matrix:
                print(f'{element_row:>5}', end="")
            print()
        return ''

    def __add__(self, other):
        if len(self.list_elements_matrix) == len(other.list_elements_matrix) and len(self.list_elements_matrix[0]) == len(other.list_elements_matrix[0]):
            new_matrix = Matrix()
            for row_number in range(len(self.list_elements_matrix)):
                row_new_matrix = []
                for element_number in range(len(self.list_elements_matrix[0])):
                    row_new_matrix.append(
                        self.list_elements_matrix[row_number][element_number] + other.list_elements_matrix[row_number][
                            element_number])
                new_matrix.list_elements_matrix.append(row_new_matrix)
            return new_matrix
        else:
            raise ValueError("Размерность матриц должна быть одинаковой")


matrix_1 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
matrix_2 = Matrix([[3, -2, -30], [1, 1, 1], [1, -64, 8]])

# print(matrix_1.__add__(matrix_2))
print(matrix_1 + matrix_2)