#!/usr/bin/python3
"""0-square module

Defines a Square class with a private size attribute.
"""


class Square:
	"""Represent a square with a private `__size` attribute."""

	def __init__(self, size=0, position=(0, 0)):
		"""Initialize a new Square.

		Args:
			size (int): The size of the new square (default 0).
			position (tuple): The position (x, y) of the square (default (0, 0)).

		Raises:
			TypeError: if `size` is not an integer or `position` is not a
				tuple of 2 positive integers.
			ValueError: if `size` is less than 0.
		"""
		self.size = size
		self.position = position

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

	@property
	def position(self):
		"""Retrieve the position."""
		return self.__position

	@position.setter
	def position(self, value):
		"""Set the position with validation.

		Args:
			value (tuple): new position as a tuple of 2 positive integers.

		Raises:
			TypeError: if `value` is not a tuple of 2 positive integers.
		"""
		if (not isinstance(value, tuple) or len(value) != 2 or
				not all(isinstance(n, int) for n in value) or
				any(n < 0 for n in value)):
			raise TypeError("position must be a tuple of 2 positive integers")
		self.__position = value

	def area(self):
		"""Return the current square area."""
		return (self.__size ** 2)

	def my_print(self):
		"""Print the square with the character # to stdout.

		If `size` is 0, prints an empty line.
		"""
		if self.__size == 0:
			print()
			return
		# vertical offset
		for _ in range(self.__position[1]):
			print()
		for i in range(self.__size):
			print(" " * self.__position[0] + "#" * self.__size)


