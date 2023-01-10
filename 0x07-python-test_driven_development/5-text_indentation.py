#!/usr/bin/python3
"""
Printing sentences with two blank lines after . ? and :
example of use

    >>> text_indentation("Holberton.School? How are you: John")
    Holberton.
    <BLANKLINE>
    School?
    <BLANKLINE>
    How are you:
    <BLANKLINE>
    John

"""


def text_indentation(text):
    """ Function implementation """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for index in range(len(text)):
        if text[index] == "." or text[index] == "?" or text[index] == ":":
            print(text[index])
            print()
        elif text[index - 1] in [".", ":", "?", " "] and text[index] == " ":
            continue

        else:
            print(text[index], end="")
