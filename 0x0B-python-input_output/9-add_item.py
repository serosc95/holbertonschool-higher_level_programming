#!/usr/bin/python3
""" Module """

import sys
import json
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


filename = 'add_item.json'
try:
    listFile = load_from_json_file(filename)
except:
    listFile = []
    for i in range(1, len(sys.argv)):
        listFile.append(sys.argv[i])
    save_to_json_file(listFile, filename)
