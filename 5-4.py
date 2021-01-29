ru_list = ['Один', 'Два', 'Три', 'Четыре']
with open('file_4.txt', encoding='utf8') as file_1:
    content = [line.split() for line in file_1]
    for i in range(len(content)):
        content[i][0] = ru_list[i]
    ru_lines = [' '.join(el) for el in content]
    print(ru_lines)
with open('file_4.ru.txt', 'w', encoding='utf8') as file_2:
    for el in ru_lines:
        file_2.write(el + '\n')
