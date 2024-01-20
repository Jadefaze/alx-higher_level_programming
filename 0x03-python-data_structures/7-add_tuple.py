#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """ Add two tuples
        first element is addition of first element
        of each tuple and so is the second, third...
        for tuples smaller than 2, use 0 for missing elements
    Args:
        tuple_a: the first tuple to add
        tuple_b: the second tuple

    Return:
        the tuple which results the addition
        """
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    list_c = [0, 0]

    if len(list_a) == 0:
        list_a.append(0)
        list_a.append(0)

    if len(list_b) == 0:
        list_b.append(0)
        list_b.append(0)

    if len(list_a) == 1:
        list_a.append(0)
    if len(list_b) == 1:
        list_b.append(0)

    if len(list_a) > 2:
        del list_a[2:]

    if len(list_b) > 2:
        del list_b[2:]

    for i in range(0, 2):
        list_c[i] = list_a[i] + list_b[i]

    tuple_c = tuple(list_c)

    return (tuple_c)
