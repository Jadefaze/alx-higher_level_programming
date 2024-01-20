#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """ print ints from list

    Args:
        my_list: the list with integers

    Returns:
        Nothing
    """
    for num in my_list:
        print("{:d}".format(num))
