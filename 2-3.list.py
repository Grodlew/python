seasons = ['Зима', 'Весна', 'Лето', 'Осень']
user_month = int(input('Введите месяц (число от 1 до 12): '))
if 1 <= user_month < 3 or 11 < user_month <= 12:
    print(seasons[0])
elif 3 <= user_month < 6:
    print(seasons[1])
elif 6 <= user_month < 9:
    print(seasons[2])
else:
    print(seasons[3])
