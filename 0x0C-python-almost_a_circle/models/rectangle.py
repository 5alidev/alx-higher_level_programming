#!/usr/bin/python3
'''
Module contains Rectangle class
'''
from models.base import Base


class Rectangle(Base):
    '''
    Rectangle class that inherits from Base class
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Rectangle class constructor
        '''

        super().__init__(id)
        self.checkIfInteger(width, "width")
        self.checkWidthHeight(width, "width")
        self.__width = width
        self.checkIfInteger(height, "height")
        self.checkWidthHeight(height, "height")
        self.__height = height
        self.checkIfInteger(x, "x")
        self.checkXandY(x, "x")
        self.__x = x
        self.checkIfInteger(y, "y")
        self.checkXandY(y, "y")
        self.__y = y

    @property
    def width(self):
        '''width getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width setter'''
        self.checkIfInteger(value, "width")
        self.checkWidthHeight(value, "width")
        self.__width = value

    @property
    def height(self):
        '''height getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height setter'''
        self.checkIfInteger(value, "height")
        self.checkWidthHeight(value, "height")
        self.__height = value

    @property
    def x(self):
        '''x getter'''
        return self.__x

    @x.setter
    def x(self, value):
        '''x setter'''
        self.checkIfInteger(value, "x")
        self.checkXandY(value, "x")
        self.__x = value

    @property
    def y(self):
        '''y getter'''
        return self.__y

    @y.setter
    def y(self, value):
        '''y setter'''
        self.checkIfInteger(value, "y")
        self.checkXandY(value, "y")
        self.__y = value

    def area(self):
        '''
        area value of the reactangle instance
        '''

        return self.__width * self.__height

    def display(self):
        '''
        prints in stdout the Rectangle instance with #
        '''

        for _ in range(self.__y):
            print()

        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        '''
        default print (str) method
        '''

        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):
        '''
        assigns an argument to each attribute

        Args:
            args: list of arguments
        '''

        if len(args) > 0 and args[0] is not None:
            self.id = args[0]
        if len(args) > 1 and args[1] is not None:
            self.__width = args[1]
        if len(args) > 2 and args[2] is not None:
            self.__height = args[2]
        if len(args) > 3 and args[3] is not None:
            self.__x = args[3]
        if len(args) > 4 and args[4] is not None:
            self.__y = args[4]

    def checkIfInteger(self, value, name):
        '''
        check if a value is an integer, if not raises Exception

        Args:
            value: value to check
            name: name of attribute
        '''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

    def checkWidthHeight(self, value, name):
        '''
        check if value of width/height <= 0

        Args:
            value: value of either width or height
            name: width or height
        '''

        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def checkXandY(self, value, name):
        '''
        check if x or y are < 0

        Args:
            value: value of either x or y
            name: x or y
        '''

        if value < 0:
            raise ValueError("{} must be >= 0".format(name))
