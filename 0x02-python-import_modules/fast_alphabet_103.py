#!/usr/bin/python3

def print_caps_alpha():
    for letter in range(ord('A'), ord('Z') + 1):
        print("{:s}".format(chr(letter)), end='')
    print()
