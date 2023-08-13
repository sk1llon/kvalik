import copy


class Matrix:

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def __add__(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Матрицы должны быть одного размера для сложения.")

        result_data = []
        for i in range(len(self.data)):
            row = [self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))]
            result_data.append(row)

        return Matrix(result_data)

    def __sub__(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Матрицы должны быть одного размера для вычитания.")

        result_data = []
        for i in range(len(self.data)):
            row = [self.data[i][j] - other.data[i][j] for j in range(len(self.data[0]))]
            result_data.append(row)

        return Matrix(result_data)

    def __mul__(self, other):
        if len(self.data[0]) != len(other.data):
            raise ValueError(
                "Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы для умножения.")

        result_data = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(other.data[0])):
                element = sum(self.data[i][k] * other.data[k][j] for k in range(len(self.data[0])))
                row.append(element)
            result_data.append(row)

        return Matrix(result_data)

    def transpose(self):
        result_data = []
        for j in range(len(self.data[0])):
            row = [self.data[i][j] for i in range(len(self.data))]
            result_data.append(row)

        return Matrix(result_data)


m1 = Matrix([[1, 2, 3], [4, 5, 6]])
m2 = Matrix([[7, 8, 9], [10, 11, 12]])

print("Матрица 1:")
print(m1)

print('Матрица 2:')
print(m2)

print('Сложение матриц:')
result_add = m1 + m2
print(result_add)

print("Вычитание матриц:")
result_sub = m1 - m2
print(result_sub)


m3 = Matrix([[1, 2], [3, 4], [5, 6]])

print("Умножение матриц:")
result_mul = m1 * m3
print(result_mul)

print("Транспонирование матрицы 1:")
print(m1.transpose())
print('Транспонирование матрицы 2:')
print(m2.transpose())
