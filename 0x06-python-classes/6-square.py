#!/usr/bin/python3

"""To define a square class"""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """instatiate with size (private)

        Args:
            size: size of the square (private)
            position: position of object on screen

        """
        self.__position = position
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

    @property
    def position(self):
        """property getter

        Returns:
            position of object on screen
        """

        return self.__position

    @position.setter
    def position(self, value):
        """
        Args:
            value: a tuple of 2 positive integers
        """

        def position(self, value):
            if not isinstance(value, tuple) or len(value) != 2:
                raise TypeError("position must be a \
                        tuple of 2 positive integers")
            if not isinstance(value[0], int) or not isinstance(value[1], int):
                raise TypeError("position must be a \
                        tuple of 2 positive integers")
            if value[0] < 0 or value[1] < 0:
                raise ValueError("position must be a \
                        tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints to stdout the square using # """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
