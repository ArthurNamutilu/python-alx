#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_vals = set()
    for num in my_list:
        if isinstance(num, int):
            unique_vals.add(num)
    return sum(unique_vals)
