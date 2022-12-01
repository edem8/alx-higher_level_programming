#!/usr/bin/python3
def uppercase(str):
    for alphabet in str:
        asc = ord(letter) - 32
        print("{}".format(chr(asc)), end="")
    print("")
