#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
# (my_list)-1 -> last element; -1=> stop b4 reaching index 0 -1=> decrement
    for i in range(len(my_list)-1, -1, -1):  # looping index of my_list
        print("{}".format(my_list[i]))
