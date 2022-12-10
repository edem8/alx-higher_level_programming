#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print()
    else:
        for list in matrix:
            for i in range(len(list)):
                if i == len(list) - 1:
                    print("{d}".format(list[i]))
                else:
                    print("{:d}".format(i), end=' ')
            print()
