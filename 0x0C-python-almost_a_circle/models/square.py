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

    def update(self, *args, **kwargs):
        '''
        update method to update attributes via *args/**kwargs
        '''

        if args and len(args) > 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        elif kwargs:
            self.id = kwargs.get("id", self.id)
            self.size = kwargs.get("size", self.size)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)

    def to_dictionary(self):
        '''
        returns the dictionary representation of a Square
        '''

        return {
                'id': self.id,
                'x': self.x,
                'size': self.width,
                'y': self.y
                }
