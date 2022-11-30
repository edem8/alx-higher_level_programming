#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        ldigit = int(repr(number)[-1])
    else:
        ldigit = number % 10
    print(f"{ldigit}", end="")
    return ldigit
