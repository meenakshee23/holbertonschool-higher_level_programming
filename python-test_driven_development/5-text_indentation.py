#!/usr/bin/python3
"""
This module writes a function that prints a text with
2 new lines after each of these characters '.', '?', and ':'.
"""

def text_indentation(text):
    """Prints text with 2 new lines after '.', '?', or ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    for char in text:
        if char in ".?:":
            line += char
            while len(line) > 0 and line[0] == " ":
                line = line[1:]
            while len(line) > 0 and line[-1] == " ":
                line = line[:-1]
            print(line)
            print()
            line = ""
        else:
            line += char

    if len(line) > 0:
        while len(line) > 0 and line[0] == " ":
            line = line[1:]
        while len(line) > 0 and line[-1] == " ":
            line = line[:-1]
        print(line)
