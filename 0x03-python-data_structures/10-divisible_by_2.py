#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = True
    if my_list[0] % 2 != 0:
        result = False
    new_list = [result]
    for i in range(1, len(my_list)):
        result = True
        if my_list[i] % 2 != 0:
            result = False
        new_list.append(result)
    return (new_list)
