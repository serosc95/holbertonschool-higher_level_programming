#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        ref = my_list[0]
        for i in range(0, len(my_list)):
            if ref < my_list[i]:
                ref = my_list[i]
        return (ref)
