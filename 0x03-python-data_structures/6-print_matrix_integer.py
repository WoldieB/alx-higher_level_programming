#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for colo in row:
            print("{:d}".format(colo), end=" " if colo != row[-1] else "")
        print()
