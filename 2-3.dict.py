seasons = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
user_month = int(input('Введите месяц (число от 1 до 12): '))
for season, months in seasons.items():
    if user_month in months:
        print(season)
