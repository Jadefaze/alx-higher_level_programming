#!/usr/bin/python3

def max_integer(my_list=[]):
    """ to find max int in list
    Args:
        my_list: the list

    Returns:
        The int or None
    """

    int_max = 0

    if len(my_list) == 0:
        return None

    for num in my_list:
        if num > int_max:
            int_max = num

    return int_max
