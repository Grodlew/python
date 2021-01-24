from itertools import count

n = 10
for el in count(n):
    if el > n + 10:
        break
    else:
        print(el)
