from sys import argv

script_name, hours, hourly_rate, bonus = argv


def pay_calc():
    return int(hours) * int(hourly_rate) + int(bonus)


print('Часы: ', hours)
print('Почасовая ставка: ', hourly_rate)
print('Премия: ', bonus)
print(f'Зарплата: {pay_calc()}')
