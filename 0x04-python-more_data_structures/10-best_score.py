#!/usr/bin/python3

def best_score(a_dictionary):

    if a_dictionary is None or not a_dictionary:
        return None

    a_list = list(a_dictionary)

    max_int = a_dictionary[a_list[0]]
    for k, v in a_dictionary.items():
        if v > max_int:
            max_int = v
            max_key = k

    return max_key
