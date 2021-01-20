def my_func(a, b, c):
    temp_list = [a, b, c]
    temp_list.sort(reverse=True)
    return temp_list[0] + temp_list[1]


print(my_func(4, 7, 5))
