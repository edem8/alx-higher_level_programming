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
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix" +
                        " (lists of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix" +
                            " (list of lists) of integers/floats")
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError("matrix must be a matrix" +
                                " (list of lists) of integers/floats")

    matrix_len = len(matrix[0])
    for row in matrix:
        if len(row) != matrix_len:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]
    return new_matrix
