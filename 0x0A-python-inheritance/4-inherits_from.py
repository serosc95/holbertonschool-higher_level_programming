#!/usr/bin/python3
""" Module """


def inherits_from(obj, a_class):
    """ Function inherits_from """
    return (isinstance(obj, a_class) and not (type(obj) == a_class))
