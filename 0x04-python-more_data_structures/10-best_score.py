#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        ref = 0
        for i in a_dictionary.keys():
            if ref < a_dictionary[i]:
                ref = a_dictionary[i]
                value = i
        return value
    return None
