n = int(input('Количество элементов: '))
my_list = []
for i in range(n):
    my_list.append(input('Введите элемент списка: '))
print(my_list)
for i in range(0, len(my_list) - 1, 2):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print(my_list)
