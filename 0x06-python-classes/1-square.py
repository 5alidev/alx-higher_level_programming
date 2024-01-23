#!/usr/bin/python3
"""Define Square class with a private attribute"""


class Square:
    """Square class with private size attribute

    Attributes:
        size (int): size of square
    """
    def __init__(self, size):
        """init to create new instance of square
        Args:
            size (int): size of square
        """
        self.__size = size
