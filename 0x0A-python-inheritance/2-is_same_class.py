#!/usr/bin/python3
'''is_same_class() function'''


def is_same_class(obj, a_class):
    '''
    test if obj is exactly an instance of a_class

    Args:
        obj: object
        a_class: class

    Returns:
        True if the object is exactly an instance of the specified class.
        otherwise False.
    '''

    return isinstance(obj, a_class)
