#!/usr/bin/python3
""" Module """


import json


class Base:
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ __init__ method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to_json_string method """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save_to_file method """
        filename = cls.__name__ + ".json"
        list_dict = []
        if list_objs is not None:
            for obj in list_objs:
                list_dict.append(cls.to_dictionary(obj))
        with open(filename, 'w') as myFile:
            myFile.write(cls.to_json_string(list_dict))
