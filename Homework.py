# 1
name = input('Ваше имя: ')
f_name = input('Ваша фамилия: ')
age = input('Ваш возраст: ')
weight = input('Ваш вес: ')
print(name, f_name, 'возраст:', age, 'вес:', weight)
# 2
time = int(input('Сколько секунд: '))
hours = time // 3600
minutes = (time % 3600) // 60
seconds = time % 60
print(f'чч:мм:сс: {hours:02d}:{minutes:02d}:{seconds:02d}')
# 3
n = input('Введите число n: ')
print(int(n) + int(n + n) + int(n + n + n))
# 4
number = int(input('Введите целое положительное число: '))
max_digit = 0
while number > 10:
    digit = number % 10
    if digit > max_digit:
        max_digit = digit
    number = number // 10
print(f'самая большая цифра: {max_digit}')
# 5
revenue = int(input('Введите выручку: '))
expenses = int(input('Введите издержки: '))
if revenue > expenses:
    print('Вы работаете в прибыль')
    profit = revenue - expenses
    print(f'Рентабельность: {profit / revenue * 100:.2f}%')
    staff = int(input('Сколько у вас сотрудников?'))
    print(f'Прибыль на одного сотрудника: {profit / staff:.2f}')
else:
    print('Вы работаете в убыток')
# 6
dist = int(input('Сколько километров вы можете пробежать: '))
goal = int(input('Ваша цель, км: '))
days = 1
while dist < goal:
    dist *= 1.1
    days += 1
print(f'Вы сможете достичь своей цели на {days}-й день.')
