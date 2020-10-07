#!/usr/bin/python3
""" Module """


def number_of_lines(filename=""):
    """ Function number_of_lines """
    with open(filename, 'r') as myFile:
        return len(myFile.readlines())
