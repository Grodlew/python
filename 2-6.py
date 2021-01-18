goods = []
goods_num = 1
while True:
    prop = input('Для добавления товара в список введите + : ')
    if prop == '+':
        prod_dict = {
            'название': input('Введите название товара: '),
            'цена': int(input('Цена: ')),
            'количество': int(input('Количество: ')),
            'ед': input('Единицы измерения: ')
        }
        i = 0
        goods.append(tuple([goods_num, prod_dict]))
        goods_num += 1
    else:
        break
for el in goods:
    print(el)

goods_dict = {}
for el in goods:
    num, g_dict = el
    for key, value in g_dict.items():
        goods_dict.setdefault(key, []).append(value)
goods_dict = {key: list(set(value)) for key, value in goods_dict.items()}
for key, value in goods_dict.items():
    print(f'{key}: {value}')