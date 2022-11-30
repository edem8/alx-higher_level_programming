#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = int(repr(number)[-1]) * -1
else:
    last_digit = number % 10
start = "Last digit of"
if last_digit > 5:
    print(f"{start} {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"{start} {number} is {last_digit} and is 0")
else:
    print(f"{start} {number} is {last_digit} and is less than 6 and not 0")
