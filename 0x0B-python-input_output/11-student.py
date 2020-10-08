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

    def class_to_json(obj):
        """ class_to_json method
        Arguments:
            self: self
        """
        return self.__dict__
