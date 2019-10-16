#!/usr/bin/python3
"""Read number of lines"""

def read_lines(filename="", nb_lines=0):
    """Return given number of lines"""
    with open(filename, encoding='utf-8') as f:
        if nb_lines < 1:
            print(f.read(), end='')
        else:
            for x in range(nb_lines):
                print(f.readline(), end='')
