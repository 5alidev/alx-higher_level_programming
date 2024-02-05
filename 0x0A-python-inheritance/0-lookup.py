#!/usr/bin/python3
'''lookup() function'''


def lookup(obj):
    '''
    return a list o available attributes and methods of obj

    Args:
        obj: Object

    Returns:
        list: available attributes and methods of obj
    '''
    return dir(obj)
