#!/usr/bin/python3
"""Get - https://intranet.hbtn.io/status"""
from urllib import request

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    with request.urlopen(url) as res:
        response = res.read()
        print("Body response:")
        print("\t- type: {}" .format(type(response)))
        print("\t- content: {}" .format(response))
        print("\t- utf8 content: {}" .format(response.decode("utf-8")))
