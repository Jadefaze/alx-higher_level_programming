#!/usr/bin/python3

def print_alphabet_upper():
    for num in range(65, 91):
        print("{:s}".format(chr(num)), end='')
    print()


if __name__ == "__main__":
    print_alphabet_upper()
