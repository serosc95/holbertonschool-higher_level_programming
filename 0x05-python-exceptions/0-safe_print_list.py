#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(0, x):
        try:
            my_list[i]
            print(my_list[i], end="")
        except:
            break
        count = count + 1
    print()
    return count
