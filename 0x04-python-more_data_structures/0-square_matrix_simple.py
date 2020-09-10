#!/usr/bin/python3
def exp2(n):
    return pow(n, 2)


def square_matrix_simple(matrix=[]):
    new_list = [list(map(exp2, i)) for i in matrix]
    return new_list
