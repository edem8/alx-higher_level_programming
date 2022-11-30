#!/usr/bin/python3
def islower(c):
    asci_letter = ord(c)
    if asci_letter in range(97, 97+26):
        return True
    else:
        return False
