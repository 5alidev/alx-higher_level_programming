#!/usr/bin/python3
"""Define Square class with a private attribute"""


class Square:
    """Square class with private size attribute

    Attributes:
        size (int): size of square
    """
    def __init__(self, size=0, position=(0, 0)):
        """init to create new instance of square
        Args:
            size (int): size of square
            position (tuple): position
        """
        self.__size = size
        self.__position = position

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
            for x in range(self.__position[1]):
                print()
            for y in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end="")
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

    @property
    def position(self):
        """retreive position"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
