class Storage:
    pass


class OfficeEquip:

    def __init__(self, brand, model, eq_type):
        self.brand = brand
        self.model = model
        self.eq_type = eq_type


class Printer(OfficeEquip):
    def __init__(self, brand, model, print_color, eq_type='принтер'):
        super().__init__(brand, model, eq_type)
        self.print_color = print_color


class Scanner(OfficeEquip):
    def __init__(self, brand, model, eq_type='сканер'):
        super().__init__(brand, model, eq_type)


class Copier(OfficeEquip):
    def __init__(self, brand, model, print_color, eq_type='ксерокс'):
        super().__init__(brand, model, eq_type)
        self.print_color = print_color
