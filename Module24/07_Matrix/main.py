import copy


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def add(self, matrix_2):
        pass
    def subtract(self, matrix_2):

        pass

    def multiply(self, matrix_2):

        pass

    def transpose(self):

        pass
    def columns(self):
        for i_elem in self.matrix:
            return len(i_elem)
    def print_result(self):
        for i_list in self.matrix:
            for i_elem in i_list:
                print(i_elem, end=' ')
            print()


m1 = Matrix([[1, 2, 3], [4, 5, 6]])

m2 = Matrix([[7, 8, 9], [10, 11, 12]])

print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("Сложение матриц:")
print(m1.add(m2))

print("Вычитание матриц:")
print(m1.subtract(m2))

m3 = Matrix([[1, 2], [3, 4], [5, 6]])

print("Умножение матриц:")
print(m1.multiply(m3))

print("Транспонирование матрицы 1:")
print(m1.transpose())
