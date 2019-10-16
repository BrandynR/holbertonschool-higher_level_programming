#!/usr/bin/python3
"""add all arguments to a python list and save to a file."""
import json
from sys import argv


loadff = __import__('8-load_from_json_file').load_from_json_file
dumptf = __import__('7-save_to_json_file').save_to_json_file


name = 'add_item.json'
try:
    f = open(name)
except:
    li = []
    for x in argv[1:]:
        li.append(x)
    dumptf(li, name)
else:
    f.close()
    jli = loadff(name)
    for x in argv[1:]:
        jli.append(x)
    dumptf(jli, name)
