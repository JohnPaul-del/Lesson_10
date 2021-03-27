class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        if len(self.matrix[0]) == len(other.matrix[0]):
            return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
                           for i in range(len(self.matrix))])
        else:
            return f"\033[31m {'Math error. Need matrices of the same size'}"

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))


matrix_1 = Matrix([[11, 15, 1], [34, 43, 23], [100, 54, 1]])
matrix_2 = Matrix([[1, 4], [44, 51], [76, 25]])

matrix_3 = matrix_1 + matrix_2
print(f"{'*'*30} First Matrix {'*'*30}\n{matrix_1}")
print(f"{'*'*30} Second Matrix {'*'*30}\n{matrix_2}")
print(f"{'*'*30} Sum of matrix {'*'*30}\n{matrix_3}")
