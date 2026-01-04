#!/usr/bin/python3
"""
Module for serializing and deserializing custom Python objects using pickle.
"""
import pickle


class CustomObject:
    """
    A custom Python class with serialization and deserialization capabilities.
    """
    
    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject.
        
        Args:
            name (str): The name of the person
            age (int): The age of the person
            is_student (bool): Whether the person is a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def display(self):
        """
        Display the object's attributes in the specified format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")
    
    def serialize(self, filename):
        """
        Serialize the current instance and save it to a file using pickle.
        
        Args:
            filename (str): The name of the file to save the serialized object to
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Error serializing object: {e}")
            return None
    
    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a pickle file and return a new instance.
        
        Args:
            filename (str): The name of the file to load the serialized object from
            
        Returns:
            CustomObject: A new instance of CustomObject, or None if an error occurs
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            print(f"Error deserializing object: {e}")
            return None
