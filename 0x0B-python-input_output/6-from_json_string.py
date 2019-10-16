#!/usr/bin/python3
"""Convert from JSON to string."""
import json


def from_json_string(my_str):
    """Return string from json object."""
    return json.loads(my_str)
