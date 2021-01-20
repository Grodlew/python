def int_func(word):
    """
    Делаем из слова список, узнаем номер первой буквы в Юникод и вычитаем 32,
    чтобы получить такую же заглавную букву, которую вставляем на место строчной.
    """
    temp_list = list(word)
    n = ord(temp_list[0]) - 32
    temp_list[0] = chr(n)
    return ''.join(temp_list)


def int_func_x(words):
    temp_list = words.split()
    for i in range(len(temp_list)):
        temp_list[i] = int_func(temp_list[i])
    return ' '.join(temp_list)


print(int_func('spam'))
print(int_func_x('some random text'))
