#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    add = 0
    for i in range(1, len(argv)):
        add = add + int(argv[i])
    print(add)
