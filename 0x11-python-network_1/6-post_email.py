#!/usr/bin/python3
"""POST request with email"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    params = {"email": sys.argv[2]}

    req = requests.post(url, data=params)
    print("{}" .format(req.text))
