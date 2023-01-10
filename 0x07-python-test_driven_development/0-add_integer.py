#!/usr/bin/python3
"""
A function that adds two integers, a and b.
Example:

>>> add_integer(2, 3) #doctest: +NOMARLIZE_WHITESPACES
5

"""


def add_integer(a, b=98):
    """ Addition function for integer and floats """
    if not type(a) in [int, float]:
        raise TypeError("a must be an integer")
    if not type(b) in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
