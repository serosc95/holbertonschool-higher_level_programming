#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
signo = 1
if number < 0:
        signo = -1
last = (number * signo) % 10
print("Last digit of {:d} is" .format(number), end=" ")
if last > 5:
        print("{:d} and is greater than 5" .format(last * signo))
elif last == 0:
        print("{:d} and is 0" .format(last * signo))
else:
        print("{:d} and is less than 6 and not 0" .format(last * signo))
