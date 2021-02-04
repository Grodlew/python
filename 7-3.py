class Cell:
    def __init__(self, cells_num):
        self.cells_num = cells_num

    def __add__(self, other):
        return Cell(self.cells_num + other.cells_num)

    def __sub__(self, other):
        return Cell(self.cells_num - other.cells_num) if self.cells_num > other.cells_num else 'Вычитание невозможно.'

    def __mul__(self, other):
        return Cell(self.cells_num * other.cells_num)

    def __truediv__(self, other):
        return Cell(round(self.cells_num / other.cells_num))

    def __str__(self):
        return f'Клетка состоит из {self.cells_num} ячеек'

    def make_order(self, n):
        string, residue = self.cells_num // n, self.cells_num % n
        return '\n'.join(['*' * n] * string + (['*' * residue] if residue else []))


cell_1 = Cell(12)
cell_2 = Cell(6)
print((cell_1 + cell_2).make_order(7))
print(cell_1 * cell_2)
print(cell_1 - cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(5))
