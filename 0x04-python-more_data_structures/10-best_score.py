#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_val = 0
    for score in a_dictionary.values():
        if score > max_val:
            max_val = score

    for key in a_dictionary.keys():
        if a_dictionary[key] == max_val:
            return key
