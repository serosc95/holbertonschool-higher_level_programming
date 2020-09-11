#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    listnew = {}
    for i, j in a_dictionary.items():
        listnew[i] = j * 2
    return listnew
