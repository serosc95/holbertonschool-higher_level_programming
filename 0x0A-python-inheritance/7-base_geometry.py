#!/usr/bin/python3


""" The class BaseGeometry """


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
