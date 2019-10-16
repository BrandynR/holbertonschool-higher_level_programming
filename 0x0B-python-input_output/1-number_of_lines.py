#!/usr/bin/python3
"""Count number of lines"""


def number_of_lines(filename=""):
    """Count  umber of lines"""
    count = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            count += 1

        return count
