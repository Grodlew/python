rating = [7, 5, 3, 3, 2]
print(rating)
while True:
    num = input('Введите число для добавления в рейтинг: ')
    if num.isdigit():
        rating.append(int(num))
        rating.sort(reverse=True)
        print(rating)
    else:
        break
