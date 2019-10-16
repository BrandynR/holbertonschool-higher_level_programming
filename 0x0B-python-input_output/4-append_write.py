#!/usr/bin/python3
"""Append string at end of text file"""


def append_write(filename="", text=""):
    """Append text to end of file"""

    with open(filename, mode='a') as f:
        return f.write(text)
