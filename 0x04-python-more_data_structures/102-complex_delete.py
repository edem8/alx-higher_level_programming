#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    for key, value in a_dictionary:
        if value in a_dictionary.values():
            a_dictionary.pop(key)
    return a_dictionary
