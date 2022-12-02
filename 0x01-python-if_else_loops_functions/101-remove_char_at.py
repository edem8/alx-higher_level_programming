#!/usr/bin/python3

def remove_char_at(str, n):
    i = 0
    new = ""
    while i < len(str):
        if i != n:
            new += str[i]
        i += 1
    return new
