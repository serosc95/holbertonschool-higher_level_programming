#!/usr/bin/python3
""" The class Rectangle"""


class Rectangle:
    """ Class Rectangle empty

        Attributes:
            __width: width
            __height: height
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ __init__ method
        Arguments:
            self: self
            width (int): width
            height (int): height
        Returns: No Value
        """
        Rectangle.number_of_instances += 1
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

    def area(self):
        """area method
        Arguments:
            self: self
        Returns: Area (int)
        """
        return self.__width * self.__height

    def perimeter(self):
        """perimeter method
        Arguments:
            self: self
        Returns: Perimeter (int)
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """__str__ method
        Arguments:
            self: self
        Returns: draw (Any type)
        """
        draw = ""
        if self.__width == 0 or self.__height == 0:
            return draw
        for i in range(self.__height):
            draw = draw + (str(self.print_symbol) * self.__width)
            if i != self.__height - 1:
                draw = draw + "\n"
        return draw

    def __repr__(self):
        """__repr__ method
        Arguments:
            self: self
        Returns: representation (string)
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """__del__ method
        Arguments:
            self: self
        Returns: No value
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """bigger_or_equal method
        Arguments:
            rect_1 (object): rect_1
            rect_2 (object): rect_2
        Returns: object biggest
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        if rect_1.area() >= rect_2.area():
            return rect_1

    @classmethod
    def square(cls, size=0):
        """square method
        Arguments:
            cls: cls
            size (int): size
        Returns: new Rectangle
        """
        new_obj = cls(size, size)
        return new_obj
