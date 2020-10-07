#!/usr/bin/python3
""" Module """


import json


def save_to_json_file(my_obj, filename):
    """ Function save_to_json_file """
    with open(filename, 'w') as myFile:
        myFile.write(json.dumps(my_obj))
