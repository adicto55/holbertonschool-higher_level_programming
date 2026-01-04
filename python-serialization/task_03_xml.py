#!/usr/bin/env python3
"""
Module for serializing and deserializing Python dictionaries using XML format.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML and save it to a file.
    
    Args:
        dictionary (dict): The Python dictionary to serialize
        filename (str): The filename to save the XML data to
    """
    try:
        # Create root element
        root = ET.Element('data')
        
        # Iterate through dictionary items and add them as child elements
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        
        # Create ElementTree and write to file
        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
    except Exception as e:
        print(f"Error serializing to XML: {e}")
        return None


def deserialize_from_xml(filename):
    """
    Deserialize a Python dictionary from an XML file.
    
    Args:
        filename (str): The filename to read the XML data from
        
    Returns:
        dict: The deserialized Python dictionary, or None if an error occurs
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # Reconstruct the dictionary by iterating through child elements
        deserialized_dict = {}
        for child in root:
            deserialized_dict[child.tag] = child.text
        
        return deserialized_dict
    except Exception as e:
        print(f"Error deserializing from XML: {e}")
        return None
