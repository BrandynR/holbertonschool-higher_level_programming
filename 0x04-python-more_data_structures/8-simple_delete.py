#!/usr/bin/python3
def simple_delete(a_dictonary, key=""):
    if key in a_dictonary.keys():
        del(a_dictonary[key])
    return (a_dictonary)
