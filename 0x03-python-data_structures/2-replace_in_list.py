#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """ to replace list element

    Args:
        my_list: the list
        idx: the idx to use
        element: what to insert

    Returns:
        my_list
    """

    if idx < 0:
        return (my_list)

    if idx is None or idx >= len(my_list):
        return (my_list)

    my_list[idx] = element

    return (my_list)
