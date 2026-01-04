#!/usr/bin/python3
"""Module for VerboseList class that extends built-in list."""


class VerboseList(list):
    """A list subclass that prints notifications for add/remove operations."""

    def append(self, item):
        """Add an item to the list and print a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """Extend the list with items and print a notification."""
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """Remove an item from the list and print a notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return an item from the list and print a notification."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        super().pop(index)
