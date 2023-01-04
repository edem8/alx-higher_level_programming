#!/usr/bin/python3
"""
A class that defines a square
    * private instance attribute : size
    Instantiation with size (no type verfication)
Hence an error might be thrown if type is wrong
"""


class Square:
    """ initialization method below """
    def __init__(self, size):
        self.__size = size
