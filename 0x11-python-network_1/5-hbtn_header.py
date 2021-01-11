#!/usr/bin/python3
"""displays the value of the variable X-Request-Id"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    print(dict(req.headers).get("x-request-id"))
