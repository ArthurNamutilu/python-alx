#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ()
    tuple_x = tuple_a + (0, 0)
    tuple_y = tuple_b + (0,0)

    tuple_c = tuple_x[0] + tuple_y[0], tuple_x[1] + tuple_y[1]
    return tuple_c
