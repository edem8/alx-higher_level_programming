#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    print_count = 0
    try:
        for i in range(x):
            if type(my_list[i]) == type(i):
                print("{:d}".format(my_list[i]), end="")
                print_count += 1
            else:
                continue
    except (NameError, TypeError, ValueError, IndexError):
        pass
    print()
    return print_count
