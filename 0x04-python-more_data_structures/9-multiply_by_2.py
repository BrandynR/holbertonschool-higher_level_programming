#!/usr/bin/python3
def multiply_by_2(a_dictonary):
    new_dictonary = {}
    for key in a_dictonary.keys():
        new_dictonary[key] = (a_dictonary[key] * 2)
    return (new_dictonary)
