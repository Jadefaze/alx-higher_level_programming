#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4 as hidden
    import sys

    names = dir(hidden)

    for name in names:
        if name == '__*':
            pass
        else:
            print(name)
