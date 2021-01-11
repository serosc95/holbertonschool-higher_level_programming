#!/usr/bin/python3
"""displays error code"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    if req.status_code == 200:
        print(req.text)
    else:
        print("Error code: {}" .format(req.status_code))
