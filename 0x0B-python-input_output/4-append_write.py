#!/usr/bin/python3
""" Module """


def append_write(filename="", text=""):
    """ Function append_write """
    with open(filename, 'a') as myFile:
        myFile.write(text)
        return len(text)
