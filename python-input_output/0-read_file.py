#!/usr/bin/python3
"""This module provides functions for file operations"""

def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout"""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())
