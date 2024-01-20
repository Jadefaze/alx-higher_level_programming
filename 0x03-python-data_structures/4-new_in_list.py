#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """ replace element without modifying list

    Args:
        my_list: the list
        idx: the index
        element: the new elememt

    Returns:
        new_list
    """
    new_list = my_list[:]

    if idx < 0 or idx >= len(my_list):
        return new_list

    new_list[idx] = element

    return (new_list)
