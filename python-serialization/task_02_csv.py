#!/usr/bin/python3
"""This module gains experience in  reading data from one format (CSV) and 
converting it into another format (JSON)"""
import csv
import json


def convert_csv_to_json(csv_filename):
     """Takes the CSV filename as its parameter and writes the JSON data to data.json"""
     try:
        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True
     except FileNotFoundError:
        return False
     