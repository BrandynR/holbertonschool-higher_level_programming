#!/usr/bin/python3
def best_score(a_dictonary):
    if a_dictionary is None or a_dictonary == {}:
        return (None)
    if isinstance(a_dictionary, dict) is False:
        return (None)
    if max(a_dictionary, key=a_dictionary.get) is 0:
        return (None)
    return(max(a_dictionary, key=a_dictionary.get))
