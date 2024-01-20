#!/usr/bin/python3

def element_at(my_list, idx):
    if not my_list or idx is None or idx >= len(my_list):
        return None

    if 0 <= idx < len(my_list):
        return my_list[idx]
    else:
        return None
