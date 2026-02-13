#!/usr/bin/python3
"""
This module writes a function that creates an
Object from a "JSON file"
"""

import json


def load_from_json_file(filename):
    """Creates an Object from JSON file"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
