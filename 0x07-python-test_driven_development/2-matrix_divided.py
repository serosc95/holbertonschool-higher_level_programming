#!/usr/bin/python3
""" This module is the same function matrix_divided
"""


def matrix_divided(matrix, div):
    """ matrix_divided function that adds 2 integers
        Args:
            matrix = is a matrix
            div = number divisor
    """
    Err = {
        "a": "matrix must be a matrix (list of lists) of integers/floats",
        "b": "Each row of the matrix must have the same size"
    }
    if matrix:
        new_matrix = []
        if not isinstance(matrix, list):
            raise TypeError(Err["a"])
        elif not isinstance(div, int) and not isinstance(div, float):
            raise TypeError("div must be a number")
        elif div == 0:
            raise ZeroDivisionError("division by zero")
        index = 0
        for x in matrix:
            if not isinstance(x, list):
                raise TypeError(Err["a"])
            elif len(x) != len(matrix[0]):
                raise TypeError(Err["b"])
            new_matrix.append([])
            for z in x:
                if isinstance(z, int) or isinstance(z, float):
                    new_matrix[index].append(round(z / div, 2))
                else:
                    raise TypeError(Err["a"])
            index = index + 1
        return new_matrix
    else:
        raise TypeError(Err["a"])
