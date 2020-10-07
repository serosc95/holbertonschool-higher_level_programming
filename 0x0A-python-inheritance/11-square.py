#!/usr/bin/python3
""" Module """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square """
    def __init__(self, size):
        """ __init__ method
        Arguments:
            self: self
            size (int): size
        Returns: No Value
        """
        super().integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """__str__ method
        Arguments:
            self: self
        Returns: string draw
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
