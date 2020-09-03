#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    print(len(argv) - 1, end=" ")
    if (len(argv) - 1) == 1:
        print("argument", end="")
    else:
        print("arguments", end="")
    if (len(argv) - 1) == 0:
        print(".")
    else:
        print(":")
    for i in range(1, len(argv)):
        print("{}: {}" .format(i, argv[i]))
