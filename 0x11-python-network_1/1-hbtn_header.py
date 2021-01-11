#!/usr/bin/python3
"""Show X-Request-Id of a request to a URL"""
from urllib import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with request.urlopen(url) as res:
        print(dict(res.headers).get("X-Request-Id"))
