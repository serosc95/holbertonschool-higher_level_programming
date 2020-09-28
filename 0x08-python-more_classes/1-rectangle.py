#!/usr/bin/python3
""" The class Rectangle"""


class Rectangle:
    """ Class Rectangle empty

        Attributes:
            __width: width
            __height: height
    """
    def __init__(self, width=0, height=0):
        """ __init__ method
        Arguments:
            self: self
            width (int): width
            height (int): height
        Returns: No Value
        """
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """ height property method
        Arguments:
            self: self
        Returns: self.__height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter method
        Arguments:
            self: self
            value (int): height
        Returns: No Value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ width property method
        Arguments:
            self: self
        Returns: self.__width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter method
        Arguments:
            self: self
            value (int): width
        Returns: No Value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
