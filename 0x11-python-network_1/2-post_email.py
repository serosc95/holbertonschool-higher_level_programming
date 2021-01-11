#!/usr/bin/python3
"""Send POST request toa URL with param Email"""
from urllib import request, parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    params = {"email": sys.argv[2]}
    req = parse.urlencode(params).encode("ascii")

    consult = request.Request(url, req)
    with request.urlopen(consult) as res:
        print(res.read().decode("utf-8"))
