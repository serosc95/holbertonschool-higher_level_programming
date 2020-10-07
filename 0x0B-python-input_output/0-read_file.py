#!/usr/bin/python3
""" Module """


def read_file(filename=""):
    """ Function read_file """
    with open(filename, 'r') as myFile:
        print(myFile.read(), end="")
