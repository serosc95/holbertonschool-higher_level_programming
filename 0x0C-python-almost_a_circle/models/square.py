#!/usr/bin/python3
""" Module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """__init__ method """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ __str__ method """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ size getter method """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter method """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update method """
        if args:
            datas = ["id", "width", "x", "y"]
            for argv in range(0, len(args)):
                setattr(self, datas[argv], args[argv])
        else:
            for i, j in kwargs.items():
                if hasattr(self, i):
                    setattr(self, i, j)

    def to_dictionary(self):
        """ to_dictionary method """
        dictionary = {}
        dictionary["id"] = self.id
        dictionary["x"] = self.x
        dictionary["size"] = self.width
        dictionary["y"] = self.y
        return dictionary
