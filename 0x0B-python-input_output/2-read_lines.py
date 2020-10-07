#!/usr/bin/python3
""" Module """


def read_lines(filename="", nb_lines=0):
    """ Function read_lines """
    with open(filename, 'r') as myFile:
        lines = 0
        read = myFile.readlines()
        for read_f in read:
            print(read_f, end="")
            lines += 1
            if nb_lines != 0 and nb_lines == lines:
                break
