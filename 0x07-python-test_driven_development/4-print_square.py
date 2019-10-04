#!/usr/bin/python3
"""
print_square: module for printing squares
"""


def print_square(size):
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for x in range(size):
        print('#' * size)
