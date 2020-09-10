#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = my_list[0]
    for i in range(1, len(my_list)):
        aux = 0
        for j in range(i - 1, -1, -1):
            if my_list[i] == my_list[j]:
                aux = 1
                break
        if aux == 0:
            result += my_list[i]
    return result
