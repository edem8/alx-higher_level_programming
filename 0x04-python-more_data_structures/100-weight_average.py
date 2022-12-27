#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    add = 0
    div = 0
    result = 0
    for tup in my_list:
        for num in tup:
            add += num
        div += tup[1]
    result = add / div
    return result
