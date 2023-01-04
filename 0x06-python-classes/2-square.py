#!/usr/bin/python3
"""
A class based off 1-square.py

Instantiation with optional size=0

raise TypeError exception is size != type(int)
raise ValueError exception if size < 0
"""


class Square:
    """ Initialization method below"""
    def __init__(self, size=0):
        try:
            if type(size) != int:
                raise TypeError
            if size < 0:
                raise ValueError
            self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
