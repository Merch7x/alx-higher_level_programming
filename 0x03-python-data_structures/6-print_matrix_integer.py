#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if isinstance(matrix, list):
        for i in zip(*matrix):
            print("{}".format(i))
