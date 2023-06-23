#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    new_set = set()

    # elements in set1 not in set2
    new_set.update(set_1.difference(set_2))

    # elements in set2 not in set1
    new_set.update(set_2.difference(set_1))

    return new_set
