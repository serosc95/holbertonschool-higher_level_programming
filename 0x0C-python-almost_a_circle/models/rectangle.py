#!/usr/bin/python3
""" Module """


Base = __import__('base').Base


class Rectangle(Base):
    """ Class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ method """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter method """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter method """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter method """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter method """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter method """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter method """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter method """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter method """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area method """
        return self.__width * self.__height

    def display(self):
        """ display method """
        if self.__width == 0:
            return ""
        for i in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """ __str__ method """
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ update method """
        if args:
            datas = ["width", "height", "x", "y"]
            super().__init__(args[0])
            for argv in range(1, len(args)):
                setattr(self, datas[argv - 1], args[argv])
        else:
            for i, j in kwargs.items():
                if hasattr(self, i):
                    setattr(self, i, j)

    def to_dictionary(self):
        """ to_dictionary method """
        dictionary = {}
        dictionary["x"] = self.__x
        dictionary["y"] = self.__y
        dictionary["id"] = self.id
        dictionary["width"] = self.__width
        dictionary["height"] = self.__height
        return dictionary
