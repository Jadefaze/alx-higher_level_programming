#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0

    if x == 0:
        return (i)
    while i < x:
        try:
            print("{}".format(my_list[i]), end="")
        except IndexError:
            break
        i += 1
    print()
    return (i)
