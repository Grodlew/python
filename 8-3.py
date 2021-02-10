class InpCheck(Exception):
    def __init__(self, msg):
        self.msg = msg


num_list = []
while True:
    data = input('Число для добавления в список, для завершения работы введите "stop": ')
    if data == 'stop':
        break
    try:
        if not data.isdigit():
            raise InpCheck('В список можно добавить только числа.')
        num_list.append(int(data))
    except InpCheck as err_msg:
        print(err_msg)

print(num_list)
