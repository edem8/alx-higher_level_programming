#!/usr/bin/python3
def uppercase(str):
    for alphabet in str:
        asc = ord(alphabet)
        if asc in range(ord(a), ord(z)+1):
            asc = asc -32
        print("{}".format(chr(asc)), end="")
    print()
