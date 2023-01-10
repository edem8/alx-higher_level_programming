#!/usr/bin/python3
"""
Module to find the max integer in a list
"""


def max_integer(lis=[]):
    """function to find and return the max integer in a list if integers
        if the list is empty, the function returns None
    """
    if len(lis) == 0:
        return None
    result = lis[0]
    i = 1
    while i < len(lis):
        if lis[i] > result:
            result = lis[i]
        i += 1
    return result
