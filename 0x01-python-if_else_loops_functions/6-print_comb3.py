#!/usr/bin/python3

for num in range(1, 100):
    if num == 89:
        print("{:02d}".format(num))
    elif num < 10:
        print("{:02d}".format(num), end=', ')
    elif str(num)[0] < str(num)[1]:
        print("{:02d}".format(num), end=', ')
