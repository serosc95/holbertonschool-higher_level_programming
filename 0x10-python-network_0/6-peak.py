#!/usr/bin/python3
""" Module """


def find_peak(list_of_integers):
    """find_peak method"""
    peak = None
    for i in range(len(list_of_integers)):
        if i > 0 and i < len(list_of_integers) - 1:
            if (list_of_integers[i] >= list_of_integers[i + 1] and
                    list_of_integers[i] >= list_of_integers[i - 1]):
                    peak = list_of_integers[i]
        else:
            if i == 0 and list_of_integers[i] >= list_of_integers[i + 1]:
                peak = list_of_integers[i]
            if i > 0 and list_of_integers[i] >= list_of_integers[i - 1]:
                peak = list_of_integers[i]
    return peak
