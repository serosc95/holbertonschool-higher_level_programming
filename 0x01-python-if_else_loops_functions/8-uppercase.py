#!/usr/bin/env python3
def uppercase(str):
    for c in str:
        upper = ord(c)
        if upper > 96 and upper < 123:
            upper = ord(c) - 32
        print("{:c}" .format(upper), end="")
    print()
