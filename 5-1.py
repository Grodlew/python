with open('file_1.txt', 'w', encoding='utf8') as file:
    print('Введите данные для записи в файл. Для прекращения записи введите пустую строку: ')
    while True:
        new_line = input()
        if new_line != '':
            file.write(new_line + '\n')
        else:
            break
