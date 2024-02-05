#!/usr/bin/python3
'''is_kind_of_class() function'''


def is_kind_of_class(obj, a_class):
    '''
    check if an object is an instance of, or if the object is an instance
    of a class that inherited from

    Args:
        obj: object
        a_class: class

    Returns: True or False
    '''

    return isinstance(obj, a_class)
