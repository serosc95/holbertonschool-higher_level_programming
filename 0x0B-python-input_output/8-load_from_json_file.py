#!/usr/bin/python3
""" Module """


import json


def load_from_json_file(filename):
    """ Function load_from_json_file """
    with open(filename, 'r') as myFile:
        return json.load(myFile)
