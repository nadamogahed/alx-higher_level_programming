#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # If the tuples have less than 2 elements, fill them with 0s
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    # Add the first two elements of each tuple
    tuple_res = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return tuple_res
