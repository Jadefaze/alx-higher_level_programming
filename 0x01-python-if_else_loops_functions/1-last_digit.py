#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit_str = str(number)[-1]
last_digit_int = int(last_digit_str)

if last_digit_int > 5:
    print(f"Last digit of {number:d} is {last_digit_int}\
 and is greater than 5")
elif last_digit_int == 0:
    print(f"Last digit of {number:d} is 0 and is 0")
else:
    print(f"Last digit of {number:d} is {last_digit_int}\
 and is less than 6 and not 0")
