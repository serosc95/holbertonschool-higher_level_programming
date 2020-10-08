#!/usr/bin/python3
""" Module """


class Student:
    """ Class Student """
    def __init__(self, first_name, last_name, age):
        """ __init__ method
        Arguments:
            self: self
            first_name: first_name
            last_name: last_name
            age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ class_to_json method
        Arguments:
            self: self
        """
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dict[key] = value
        return new_dict
