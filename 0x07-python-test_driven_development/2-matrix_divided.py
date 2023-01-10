#!/usr/bin/python3
"""
A function that divides elements of a matrix
Example:
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

    >>> matrix_divided(2, 3) #doctest: +ELLIPSIS
    Traceback (most recent call last):
    TypeError: ...

"""


def matrix_divided(matrix, div):
    """ Matrix division implementation """
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or (len(matrix) == 0):
        raise TypeError("matrix nust be a matrix (list of lists) of" +
                        " integers/floats")
    if type(matrix[0]) is not list or (len(matrix[0]) == 0):
        raise TypeError("matrix nust be a matrix (list of lists) of" +
                        " integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of" +
                            " integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the" +
                            " same size")
        for c in row:
            if type(c) is not int and type(c) is not float:
                raise TypeError("matrix must be a matrix (list of lists)" +
                                " of integers/floats")
    return [[round(item / div, 2) for item in row] for row in matrix]
