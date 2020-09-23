#!/usr/bin/python3
"""The class Square"""


class Square:
    """Class Square empty

    Attributes:
       __size: size
    """
    def __init__(self, size=0):
        """__init__ method

        Arguments:
        self: self
        size (int): size
        Returns: No Value
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area method

        Arguments:
        self: self
        Returns: Area (int)
        """
        return self.__size ** 2

    @property
    def size(self):
        """size method

        Arguments:
        self: self
        Returns: size (int)
        """
        return self.__size

    @size.setter
    def size(self, size):
        """size method

        Arguments:
        self: self
        size (int): size
        Returns: No Value
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
