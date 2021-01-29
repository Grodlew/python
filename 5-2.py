with open('file_2.txt') as file:
    content = file.readlines()
    print(f'Количество строк в файле: {len(content)}')
    for el in range(len(content)):
        print(f'{el + 1} строка: {len(content[el].split())} слов.')
