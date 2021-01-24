from itertools import cycle

new_list = [1, 2, 3]
c = 0
for el in cycle(new_list):
    if c > 10:
        break
    print(el)
    c += 1
