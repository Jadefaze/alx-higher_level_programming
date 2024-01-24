#!/usr/bin/pyhon3

def uniq_add(my_list):
    """ to add unique elements in list

    Args:
        my_list: the list of ints

    Returns:
        the result (sum)
    """

    """ make a set to eleminate duplicates"""

    sum_uniq = 0

    my_list_unique = list(set(my_list))

    for num in my_list_unique:
        sum_uniq += num

    return sum_uniq
