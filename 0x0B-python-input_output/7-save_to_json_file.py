#!/usr/bin/python3
"""Write json to txt file."""
import json


def save_to_json_file(my_obj, filename):
    """converts to json and saves to a file."""
    with open(filename, 'wt') as f:
        json.dump(my_obj, f)
