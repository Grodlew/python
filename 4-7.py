from math import factorial


def fact(n):
    for x in [factorial(i) for i in range(1, n + 1)]:
        yield x


for el in fact(5):
    print(el)
