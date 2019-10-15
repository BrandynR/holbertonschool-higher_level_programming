#!/usr/bin/python3
"""Adds a function to attempt to add attributes to objects."""


def add_attribute(obj, name, value):
    """Attempts to add a value to an object"""

    if hasattr(obj, '__dict__') and not hasattr(obj, '__slots__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
