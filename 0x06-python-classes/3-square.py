#!/usr/bin/python3

"""To define a square class"""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """instatiate with size (private)

        Args:
            size: size of the square (private)

        """
        if (size != 0 and not isinstance(size, int)):
            raise TypeError('size must be an integer')
        elif (size < 0):
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """To find area of the square

        Returns:
            Area of the square
        """

        return (self.__size * self.__size)
