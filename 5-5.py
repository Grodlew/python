from random import randint
with open('file_5.txt', 'r+') as file:
    file.write(' '.join([str(randint(0, 50)) for el in range(10)]))
    file.seek(0)
    content = file.read()
    my_sum = sum(int(el) for el in content.split())
    print(f'Сумма чисел в файле: {my_sum}')
