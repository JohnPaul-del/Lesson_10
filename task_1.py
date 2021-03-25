import numpy as np

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        res = []
        if len(self.matrix[0]) == len(other.matrix[0]):
            res = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
                   for i in range(len(self.matrix))]
        else:
            pass
        return Matrix(res)

    def __str__(self):
        for i in range(len(self.matrix)):
            print(*self.matrix[i])


matrix_1 = Matrix([[11, 15, 1], [34, 43, 23], [100, 54, 1]])
matrix_2 = Matrix([[1, 4], [51, 15], [25, 90]])

matrix_3 = matrix_1 + matrix_2
print(f"{'*'*30} First Matrix {'*'*30}")
matrix_1.__str__()
print(f"{'*'*30} Second Matrix {'*'*30}")
matrix_2.__str__()
print(f"{'*'*30} Summ of matrix {'*'*30}")
matrix_3.__str__()
