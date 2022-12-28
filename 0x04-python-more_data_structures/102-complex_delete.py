#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    for key in a_dictionary.keys():
        if a_dictionary[key] == value:
            a_dictionary.pop(key)
            a_dictionary = a_dictionary
    return a_dictionary
