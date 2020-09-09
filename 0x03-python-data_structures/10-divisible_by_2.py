#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        result = True
        if my_list[0] % 2 != 0:
            result = False
        new_list = [result]
        if len(my_list) > 1:
            for i in range(1, len(my_list)):
                result = True
                if my_list[i] % 2 != 0:
                    result = False
                new_list.append(result)
        return (new_list)
