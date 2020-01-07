#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """function thats finds a peak in a list of unsorted integers"""
    l_int = list_of_integers
    length = len(l_int)

    if l_int == []:
        return None
    if length == 0:
        return
    if length == 1:
        return (l_int[0])

    for i in range(0, length - 1):
        if l_int[i] > l_int[i + 1]:
            return (l_int[i])
    return (l_int[i + 1])
