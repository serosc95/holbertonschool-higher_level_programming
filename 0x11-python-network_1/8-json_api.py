#!/usr/bin/python3
"""sends a POST request to http://0.0.0.0:5000/search_user"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 1:
        params = {"q": ""}
    else:
        params = {"q": sys.argv[1]}
    req = requests.post(url, data=params)
    try:
        res = req.json()
        if res != {}:
            name = res.get("name")
            id = res.get("id")
            print("[{}] {}" .format(id, name))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
