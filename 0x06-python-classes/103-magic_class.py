#!/usr/bin/python3
"""
Define a magic class that executes the bytecode provided
"""
import math


class MagicClass:
    """Represents a circle"""
    def __init__(self, radius=0):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the MagicClass"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Returns the circumference of the MagicClass"""
        return (2 * math.pi * self.__radius)
