#!/usr/bin/python3
"""Module for CountedIterator that tracks iteration count."""


class CountedIterator:
    """An iterator that counts the number of items iterated."""

    def __init__(self, iterable):
        """Initialize the CountedIterator with an iterable.

        Args:
            iterable: An iterable object to iterate over.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Return the next item from the iterator and increment counter.

        Returns:
            The next item from the iterator.

        Raises:
            StopIteration: When there are no more items to iterate.
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Return the number of items iterated so far.

        Returns:
            The count of items that have been iterated.
        """
        return self.count
