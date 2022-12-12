#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list):
        return my_list
    new_list = []
    for num in my_list:
        if my_list.index(num) != idx:
            new_list.append(num)
    my_list = new_list
    return my_list
