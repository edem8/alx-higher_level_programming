#!/usr/bin/python3

def remove_char_at(str, n):
    new = ""
    while i < len(str):
        if i != n:
            new += str[i]
        i += 1
    return new
