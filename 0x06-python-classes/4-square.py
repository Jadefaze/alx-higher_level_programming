#!/usr/bin/python3

"""To define a square class"""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """instatiate with size (private)

        Args:
            size: size of the square (private)

        """
        self.__size = size

    def area(self):
        """To find area of the square

        Returns:
            Area of the square
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """To retrieve size of object

        Returns:
            Size of the object
        """
        return self.__size
    @size.setter
    def size(self, value):
        """property setter

        Args:
            value: the integer to set as size

        Returns:
            Nothing
        """
        if (value != 0 and not isinstance(value, int)):
            raise TypeError('size must be an integer')
        elif (value < 0):
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

