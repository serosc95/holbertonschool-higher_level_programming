#!/usr/bin/python3
for i in range(0, 9):
    for j in range(1, 10):
        if j > i and (i != 8 or j != 9):
            print("{:d}{:d}" .format(i, j), end=", ")
print("{:d}{:d}" .format(i, j))
