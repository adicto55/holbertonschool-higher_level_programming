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
		self.size = size

	@property
	def size(self):
		"""Retrieve the size."""
		return self.__size

	@size.setter
	def size(self, value):
		"""Set the size with validation.

		Args:
			value (int): new size value.

		Raises:
			TypeError: if `value` is not an integer.
			ValueError: if `value` is less than 0.
		"""
		if not isinstance(value, int):
			raise TypeError("size must be an integer")
		if value < 0:
			raise ValueError("size must be >= 0")
		self.__size = value

	def area(self):
		"""Return the current square area."""
		return (self.__size ** 2)


