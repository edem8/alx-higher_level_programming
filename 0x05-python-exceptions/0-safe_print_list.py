#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        j = 0
        for i in range(x + 1):
            print(my_list[i], end="")
            j += 1
    except IndexError:
        print()
    return j
