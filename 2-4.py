user_list = input('Введите несколько слов через пробел: ').split()
for el in user_list:
    print(f'{user_list.index(el) + 1}. {el[0:10]}')
