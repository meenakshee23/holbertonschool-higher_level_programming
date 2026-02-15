#!/usr/bin/env python3
"""
This module gain experience in reading data from one format (CSV)
and converting it into another format (JSON) using serialization techniques
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Takes the CSV filename as its parameter"""
    try:
        with open(csv_filename, newline='') as f:
            data = list(csv.DictReader(f))
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)
        return True
    except:
        return False
