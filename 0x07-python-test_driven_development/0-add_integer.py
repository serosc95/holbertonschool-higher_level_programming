#!/usr/bin/python3
""" This module is the same function add_integer
"""


def add_integer(a, b=98):
    """ add_integer function that adds 2 integers
        Args:
            a = is a integer
            b = is a integer
        Return:
            The sum if is success
    """
    try:
        sum = a + b
        return int(round(a)) + int(round(b))
    except TypeError:
        if isinstance(a, int):
            raise TypeError("b must be an integer")
        elif isinstance(b, int):
            raise TypeError("a must be an integer")
