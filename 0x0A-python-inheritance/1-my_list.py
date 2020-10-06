#!/usr/bin/python3


""" The class MyList"""


class MyList(list):
    """ Class MyList inherits from list """
    def print_sorted(self):
        """ prints the list, but sorted """
        print(sorted(self))
