#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    dif_set1 = set_1 - set_2
    dif_set2 = set_2 - set_1

    dif_set_all = dif_set1 | dif_set2

    return dif_set_all
