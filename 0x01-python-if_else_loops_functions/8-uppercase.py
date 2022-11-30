#!/usr/bin/python3
def uppercase(str):
    ln = len(str)
    for w in str[:ln + 1]:
        print("{}".format(w.capitalize), end="")
    print("")
