#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for s in my_string:
        if ord(s) != 99 and ord(s) != 67:
            new = new + s
    return(new)
