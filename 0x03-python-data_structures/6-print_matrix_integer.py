#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print()
    else:
        for list in matrix:
            for i in list:
                print(" ".join("{:d}".format(i)))
