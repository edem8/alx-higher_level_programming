#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
       ldigit = int(repr(ldigit)[-1])
    else:
        ldigit = number % 10
    return ldigit
