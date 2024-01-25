#!/usr/bin/python3

def best_score(a_dictionary):

    if not a_dictionary:
        return None

    a_list = list(a_dictionary)

    max_int = a_dictionary[a_list[0]]
    for key in a_dictionary:
        if a_dictionary[key] > max_int:
            max_key = key

    return max_key
