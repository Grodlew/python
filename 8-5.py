class Storage:
    def __init__(self):
        self.storage = {}
        self.transferred = {}

    def add(self, equip, n=1):
        for i in range(n):
            self.storage.setdefault(equip.equip_type(), []).append(equip)

    def transfer(self, eq_type, department):
        if self.storage[eq_type]:
            self.transferred.setdefault(department, []).append(self.storage.setdefault(eq_type).pop(0))

    def equip_num(self, eq_type):
        return f'{eq_type}: {len(self.storage[eq_type])}'


class OfficeEquip:

    def __init__(self, brand, model, eq_type):
        self.brand = brand
        self.model = model
        self.eq_type = eq_type

    def equip_type(self):
        return f'{self.eq_type}'

    def __repr__(self):
        return f'{self.brand} {self.model}'


class Printer(OfficeEquip):
    def __init__(self, brand, model, print_color, eq_type='принтер'):
        super().__init__(brand, model, eq_type)
        self.print_color = print_color

    def __repr__(self):
        return f'{self.brand} {self.model} {self.print_color}'


class Scanner(OfficeEquip):
    def __init__(self, brand, model, eq_type='сканер'):
        super().__init__(brand, model, eq_type)

    def __repr__(self):
        return f'{self.brand} {self.model}'


class Copier(OfficeEquip):
    def __init__(self, brand, model, print_color, eq_type='ксерокс'):
        super().__init__(brand, model, eq_type)
        self.print_color = print_color

    def __repr__(self):
        return f'{self.brand} {self.model} {self.print_color}'


print_1 = Printer('HP', 'M404n', 'ч/б')
print_2 = Printer('HP', '150nw', 'цветной')
scan = Scanner('Epson', 'DS-1660W')
copy = Copier('Canon', 'C1225iF', 'цветной')
store = Storage()
store.add(print_1, 2)
store.add(print_2)
store.add(scan, 4)
store.add(copy, 6)
print(store.storage)
print(store.equip_num('принтер'))
store.transfer('принтер', 'отдел продаж')
store.transfer('ксерокс', 'отдел логистики')
print(store.equip_num('принтер'))
print(store.transferred)
