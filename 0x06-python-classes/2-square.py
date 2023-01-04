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
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
