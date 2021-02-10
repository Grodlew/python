class ZeroDivErr(Exception):
    def __init__(self, msg):
        self.msg = msg


try:
    dividend, divider = map(float, input('Делимое и делитель через пробел: ').split())
    if divider == 0:
        raise ZeroDivErr('Делить на ноль нельзя.')
    result = dividend / divider
    print(f'{dividend} / {divider} = {result}')
except ValueError:
    print('Ошибка ввода.')
except ZeroDivErr as err_msg:
    print(err_msg)
