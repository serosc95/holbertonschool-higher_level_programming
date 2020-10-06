#!/usr/bin/python3
""" Module """


class BaseGeometry:
    """ Class BaseGeometry """
    def area(self):
        """area method
        Arguments:
            self: self
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator method
        Arguments:
            self: self
            name: name
            value: value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer" .format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0" .format(name))


""" The class Rectangle """


class Rectangle(BaseGeometry):
    """ Class Rectangle """
    def __init__(self, width, height):
        """ __init__ method
        Arguments:
            self: self
            width (int): width
            height (int): height
        Returns: No Value
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
