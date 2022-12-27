#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    add = 0
    div = 0
    mul = 1
    for tup in my_list:
        for num in tup:
            mul *= num
        add += mul
        div += tup[1]
        mul = 1

    result = add / div
    return result
