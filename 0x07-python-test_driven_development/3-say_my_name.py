#!/usr/bin/python3
"""
    say_my_name: prints  the given name
"""


def say_my_name(first_name, last_name=""):
    """
    Recieves two values, checks if they're both strings
    Elseraises a TypeError
    Returns  printed name, prefaced with `My name is`.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
