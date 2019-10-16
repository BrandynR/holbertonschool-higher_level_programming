#!/usr/bin/python3
""" Module """


def read_file(filename=""):
    """ read file and print to stdout """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')
