class Matrix:
    def __init__(self, mtx_list):
        self.matrix = mtx_list

    def __str__(self):
        return '\n'.join('\t'.join(map(str, line)) for line in self.matrix)

    def __add__(self, other):
        result = []
        for item in zip(self.matrix, other.matrix):
            result.append([sum([j, k]) for j, k in zip(*item)])
        return Matrix(result)


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6]])
print(matrix_1, '\n')
matrix_2 = Matrix([[7, 8, 9], [10, 11, 12]])
print(matrix_2, '\n')
res_matrix = matrix_1 + matrix_2
print(f'Сумма матриц:\n{res_matrix}')
