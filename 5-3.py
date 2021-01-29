with open('file_3.txt', encoding='utf8') as file:
    staff_list = [line.split() for line in file]
    print('Сотрудники с зарплатой ниже 20000:')
    for name, pay in staff_list:
        if float(pay) < 20000:
            print(name, pay)
    average_pay = sum(float(el[1]) for el in staff_list) / len(staff_list)
    print(f'Средняя зарплата: {round(average_pay, 2)}')
