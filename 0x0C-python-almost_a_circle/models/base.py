#!/usr/bin/python3
'''
module containing Base Class
'''


class Base:
    '''
    class Base with private class attribute and a class constructor

    Attributes:
        __nb_objects: number of instances created by Base class
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Base class constructor

        Args:
            id: integer
        '''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
