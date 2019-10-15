#!/usr/bin/python3
"""Class"""


class MyList(list):
    """Class inherits from list"""
    def print_sorted(self):
        print(sorted(self))
