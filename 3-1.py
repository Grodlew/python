def my_func(x, y):
	if y == 0:
		return 'Ошибка: деление на ноль.'
	return x / y


num1 = int(input('Введите делимое: '))
num2 = int(input('Введите делитель: '))
print(f'{num1} / {num2} = {my_func(num1, num2)}')