#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """ find multiples of 2

    Args:
        my_list: the list of ints

    Return:
        new_list of True/False
    """

    new_list = []

    for num in my_list:
        if num % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
