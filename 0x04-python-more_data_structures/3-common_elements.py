#!/usr/bin/python3

def common_elements(set_1, set_2):
    common_set = set()

    for num in set_1:
        if num in set_2:
            common_set.add(num)

    return common_set
