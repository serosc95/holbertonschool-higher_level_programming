#!/usr/bin/python3
"""Access Github"""
import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/user"
    auth = requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get(url, auth=auth)
    print(req.json().get("id"))
