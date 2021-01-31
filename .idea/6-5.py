class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки инструментом {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки инструментом {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки инструментом {self.title}'


p = Pen('Ручка')
pl = Pencil('Карандаш')
mk = Handle('Маркер')
print(p.draw())
print(pl.draw())
print(mk.draw())
