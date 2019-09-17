#!/usr/bin/python3
def no_c(string):

    new = ""
    for char in string:
        if char == 'c' or char == 'C':
            continue
        new += char
    return new
