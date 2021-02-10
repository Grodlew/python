class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def int_date(cls, date):
        return [int(el) for el in date.split('-')]

    @staticmethod
    def valid_date(date):
        day, month, year = [int(el) for el in date.split('-')]
        num_of_days = 28 + (month + int(month / 8)) % 2 + 2 % month + 2 * int(1 / month)
        leap_year = bool((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)
        if month == 2:
            num_of_days += leap_year
        if all([0 < day <= num_of_days and 1 <= month <= 12 and year > 0]):
            return f'{date} дата в порядке'
        else:
            return f'{date} неверная дата'


d_1 = '30-04-2009'
d_2 = '29-02-1700'
d_3 = '29-02-1600'
print(Date.int_date(d_1))
print(Date.valid_date(d_1))
print(Date.valid_date(d_2))
print(Date.valid_date(d_3))
