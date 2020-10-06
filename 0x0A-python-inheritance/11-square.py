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

    def area(self):
        """area method
        Arguments:
            self: self
        Returns: Area (int)
        """
        return self.__width * self.__height

    def __str__(self):
        """__str__ method
        Arguments:
            self: self
        Returns: string draw
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


""" The class Square """


class Square(Rectangle):
    """ Class Square """
    def __init__(self, size):
        """ __init__ method
        Arguments:
            self: self
            size (int): size
        Returns: No Value
        """
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """__str__ method
        Arguments:
            self: self
        Returns: string draw
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
