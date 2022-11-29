#!/usr/bin/python3
for i in range(97, 97+26):
    if i == 113 or i == 101:
        continue
    print("{}".format(chr(i)), end="")
