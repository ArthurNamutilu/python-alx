#!/usr/bin/python3
my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = my_list[:]
print(new_list)
my_list.append(99)
print(my_list)
print(new_list)
