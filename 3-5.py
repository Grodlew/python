def my_sum(sum_list):
    return sum([int(item) for item in sum_list])


result = 0
while True:
    user_inp = input('Введите несколько чисел через пробел. Для прекращения суммирования введите +: ').split()
    if '+' in user_inp:
        user_inp.remove('+')
        result += my_sum(user_inp)
        print(f'Сумма всех чисел: {result}')
        break
    else:
        result += my_sum(user_inp)
        print(f'Сумма всех чисел: {result}')
