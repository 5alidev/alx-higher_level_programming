#!/usr/bin/python3
"""Locked Class"""


class LockedClass:
    '''
    prevents the user from dynamically creating new instance
    attributes, except if the new instance attribute is called first_name

    Attributes:
        first_name: first name
    '''

    __slots__ = ["first_name"]

    def __init__(self):
        """new instance of class"""

        self.first_name = "first_name"
