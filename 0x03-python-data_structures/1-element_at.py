#!/usr/bin/python3

def element_at(my_list, idx):
    if not my_list:
        return None
    if idx is None or idx >= len(my_list):
        return None

    return my_list[idx]
