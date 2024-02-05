#!/usr/bin/python3
'''
MyInt class
'''


class MyInt(int):
    '''
    class MyInt that inherits from int class
    '''

    def __init__(self, value):
        '''
        MyInt constructor

        Args:
            value: integer value
        '''

        self.__value = value

    def __eq__(self, other):
        '''
        override equal method

        Args:
            other: other instance of int
        '''

        return self.__value != other

    def __ne__(self, other):
        '''
        override not equal method

        Args:
            other: other instance of int
        '''

        return self.__value == other
