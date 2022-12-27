#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [list(map((lambda x: x ** 2), matrix[0])),
                  list(map((lambda x: x ** 2), matrix[1])),
                  list(map((lambda x: x ** 2), matrix[2]))]
    return new_matrix
