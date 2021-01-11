#!/usr/bin/python3
"""Display the body in utf-8"""
from urllib import request, error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = request.Request(url)
    try:
        with request.urlopen(req) as res:
            print(res.read().decode("ascii"))
    except error.HTTPError as err:
        print("Error code: {}" .format(err.code))
