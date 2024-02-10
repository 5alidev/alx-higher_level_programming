#!/usr/bin/python3
'''
module contains Square class
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    class Square that inherits from Rectangle class
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''
        Square Constructor
        '''

        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''
        overriding __str__ method
        '''

        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''
        size getter method
        '''

        return self.width

    @size.setter
    def size(self, value):
        '''
        size setter method
        '''

        self.width = value
        self.height = value
