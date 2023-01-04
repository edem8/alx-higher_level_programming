#!/usr/bin/python3
"""
 A class square tat defines a square, based on 2-square.py

 Addition of public instance method: def area(self)
"""


class Square:
    """ Addition of an area instance method to class """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def area(self):
        return self.__size ** 2
