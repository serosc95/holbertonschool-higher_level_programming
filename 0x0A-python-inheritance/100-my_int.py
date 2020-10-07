#!/usr/bin/python3
""" The class MyInt """


class MyInt(int):
    """ Class MyInt """
    def __eq__(self, other):
        """__eq__ method
        Arguments:
            self: self
            other: other
        """
        return (int(self) != int(other))

    def __ne__(self, other):
        """__ne__ method
        Arguments:
            self: self
            other: other
        """
        return (int(self) == int(other))
