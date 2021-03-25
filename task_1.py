class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        res = []
        summ_numbers = []
        if len(self.matrix[0]) == len(other.matrix[0]):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    summ = self.matrix[i][j] + other.matrix[i][j]
                    summ_numbers.append(summ)
                    if len(summ_numbers) == len(self.matrix):
                        res.append(summ_numbers)
                        summ_numbers = []
        else:
            print("ss")

        return Matrix(res)

    def __str__(self):
        for i in range(len(self.matrix)):
            print(*self.matrix[i])


matrix_1 = Matrix([[11, 15, 1], [34, 43, 23], [100, 54, 1]])
matrix_2 = Matrix([[1, 4, 4], [15, 6, 5], [90, 67, 100]])

matrix_3 = matrix_1 + matrix_2
print(f"{'*'*30} First Matrix {'*'*30}")
matrix_1.__str__()
print(f"{'*'*30} Second Matrix {'*'*30}")
matrix_2.__str__()
print(f"{'*'*30} Summ of matrix {'*'*30}")
matrix_3.__str__()
