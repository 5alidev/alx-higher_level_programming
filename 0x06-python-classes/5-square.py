#!/usr/bin/python3
"""Define Square class with a private attribute"""


class Square:
    """Square class with private size attribute

    Attributes:
        size (int): size of square
    """
    def __init__(self, size=0):
        """init to create new instance of square
        Args:
            size (int): size of square
        """
        self.__size = size

    def area(self):
        """returns the current square area
        """
        area = self.__size * self.__size
        return area

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size <= 0:
            print()
        else:
            for x in range(0, self.__size):
                print("#" * (self.__size))

    @property
    def size(self):
        """retreive size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter
        Args:
            value (int): size of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
