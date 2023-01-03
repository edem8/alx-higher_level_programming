#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(vaue))
    except TypeError:
        pass
    if isinstance(value, int):
        return True
    else:
        return False
