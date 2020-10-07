#!/usr/bin/python3
""" Module """


def write_file(filename="", text=""):
    """ Function write_file """
    with open(filename, 'w') as myFile:
        myFile.write(text)
        return len(text)
