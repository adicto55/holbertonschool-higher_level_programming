#!/usr/bin/python3
"""0-square module

Defines a Square class with a private size attribute.
"""


class Square:
	"""Represent a square with a private `__size` attribute."""

	def __init__(self, size=0):
		"""Initialize a new Square.

		Args:
			size (int): The size of the new square (default 0).

		Raises:
			TypeError: if `size` is not an integer.
			ValueError: if `size` is less than 0.
		"""
		if not isinstance(size, int):
			raise TypeError("size must be an integer")
		if size < 0:
			raise ValueError("size must be >= 0")
		self.__size = size

	def area(self):
		"""Return the current square area."""
		return (self.__size ** 2)
