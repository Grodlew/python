def my_func(x, y):
    return x ** y


print(my_func(3.14, -3))


def my_func2(x, y):
    res = 1
    for i in range(abs(y)):
        res /= x
    return res


print(my_func(3.14, -3))
