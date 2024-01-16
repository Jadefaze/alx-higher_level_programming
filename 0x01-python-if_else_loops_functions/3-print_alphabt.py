#!/usr/bin/python3
for number in range(97, 123):
    if number == 101 or number == 113:
        pass
    else:
        print("{:c}".format(number), end='')
