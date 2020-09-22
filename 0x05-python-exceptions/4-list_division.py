#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [None] * list_length
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            div = 0
            print("wrong type")
        except:
            div = 0
            if my_l_2[i] == 0:
                print("division by 0")
            elif i >= len(my_l_1) or i >= len(my_l_2):
                print("out of range")
        new_list[i] = div
    return new_list
