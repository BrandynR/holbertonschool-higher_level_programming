#!/usr/bin/python3
"""
add_integer:
is an addition module
"""


def add_integer(a, b):
    """
    Adds two integers together.
    a and b must be integers or floats,
    If not, a TypeError exception is raised

    Returns an integer: the addition of a + b
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (a + b)
