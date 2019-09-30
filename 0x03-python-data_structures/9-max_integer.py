#!/usr/bin/python3
def max_integer(list=[]):
    if (len(list) <= 0 or list is None):
        return (None)
    maxval = list[0]
    for item in list:
        if item >= maxval:
            maxval = item
    return (maxval)
