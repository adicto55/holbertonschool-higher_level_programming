#!/usr/bin/python3
"""
Module for converting CSV data to JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert data from a CSV file to JSON format and save to data.json.
    
    Args:
        csv_filename (str): The name of the CSV file to read from
        
    Returns:
        bool: True if conversion was successful, False otherwise
    """
    try:
        # Read CSV file and convert to list of dictionaries
        data = []
        with open(csv_filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
        
        # Write the serialized JSON data to data.json
        with open('data.json', 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)
        
        return True
    except Exception as e:
        print(f"Error converting CSV to JSON: {e}")
        return False
