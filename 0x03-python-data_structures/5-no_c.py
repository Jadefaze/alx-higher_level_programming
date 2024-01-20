#!/usr/bin/python3

def no_c(my_string):
    """ to remove all c's and C's from string

    Args:
        my_string: the string with change

    Returns:
        new string
    """

    i = 0
    new_string = ""

    while i < len(my_string):
        if my_string[i] == 'c' or my_string[i] == 'C':
            pass
        else:
            new_string += my_string[i]
        i += 1

    return (new_string)
