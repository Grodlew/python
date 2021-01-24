from random import randint

my_list = [randint(1, 300) for i in range(15)]
print(my_list)
new_list = [my_list[el + 1] for el in range(len(my_list) - 1) if my_list[el + 1] > my_list[el]]
print(new_list)
