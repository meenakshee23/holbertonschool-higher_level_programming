#!/usr/bin/python3
"""This module writes a string to a text file"""


def write_file(filename="", text=""):
    """Returns the number of characters written"""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
