#!/usr/bin/python3
'''
Square class
'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    class Square that inherits from class Rectangle
    '''

    def __init__(self, size):
        '''
        Square contructor

        Args:
            size : size of square
        '''

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''
        area of Square

        Returns:
            area of square
        '''
        return self.__size ** 2

    def __str__(self):
        '''
        default print method
        '''

        return "[Square] {}/{}".format(self.__size, self.__size)
