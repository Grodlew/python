from collections import Counter

ol_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
c = Counter(ol_list)
new_list = [el for el in ol_list if c[el] == 1]
print(ol_list)
print(new_list)
