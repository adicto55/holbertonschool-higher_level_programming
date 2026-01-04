#!/usr/bin/env python3
"""
Module for basic serialization of Python dictionaries to JSON files.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to JSON and save it to a file.
    
    Args:
        data: A Python Dictionary with data
        filename: The filename of the output JSON file. 
                 If the file already exists it will be replaced.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load and deserialize data from a JSON file.
    
    Args:
        filename: The filename of the input JSON file
        
    Returns:
        A Python Dictionary with the deserialized JSON data from the file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
