#!/usr/bin/python3

def uppercase(str):
    """change into uppercase"""

    for letter in str:
        num = ord(letter)
        if num >= 97 and num <= 122:
            num = num - 32
        print("{:c}".format(num), end='')

    print()
