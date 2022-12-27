#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for List in matrix:
        new_matrix.append(list(map(lambda x: x ** 2, List)))
    return new_matrix
