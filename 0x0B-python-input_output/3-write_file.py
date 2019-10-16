#!/usr/bin/python3
"""  Write string to text file and return num of chars written"""

def write_file(filename="", text=""):
    """ Write string to text file and return num of chars written"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
