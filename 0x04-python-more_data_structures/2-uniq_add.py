#!/usr/bin/python3
def uniq_add(my_list=[]):
    if isinstance(my_list, list):
        newlist = set(my_list)
        result = 0
        for i in newlist:
            result += i
        return result
