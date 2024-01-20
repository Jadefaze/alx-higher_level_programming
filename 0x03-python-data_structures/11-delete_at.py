#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """ to delete list item given index

    Args:
        my_list: the list of items
        idx: index of item to delete from my_list

    Returns:
        the modified list
    """

    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        del my_list[idx]

    return my_list
