class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


p = Position('Иван', 'Петров', 'грузчик', 10000, 5000)
print(p.name, p.surname, p.position)
print(p.get_full_name())
print(p.get_total_income())
