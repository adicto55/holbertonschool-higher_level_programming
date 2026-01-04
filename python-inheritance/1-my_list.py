#!/usr/bin/python3
"""Module for MyList class that inherits from list"""


class MyList(list):
    """Class that inherits from list with a print_sorted method"""
    
    def print_sorted(self):
        """Print the list sorted in ascending order"""
        print(sorted(self))
