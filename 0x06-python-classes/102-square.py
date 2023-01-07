#!/usr/bin/python3
"""
A class square based on 3-sqaure.py
"""


class Square:
    """ This class adds a getter and setter method """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

    def __eq__(self, other):
        """define the == comparison to another instance"""
        return self.area() == other.area()

    def __ne__(self, other):
        """define the != comparison to anothr instance"""
        return self.area() != other.area()

    def __lt__(self, other):
        """defines the < comaprison"""
        return self.area() < other.area()

    def __le__(self, other):
        """defines the <= comaparison"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """defines the > comparison"""
        return self.area() > other.area()

    def __ge__(self, other):
        """defines the >= comparison"""
        return self.area() >= other.area()
