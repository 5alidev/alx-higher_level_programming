#!/usr/bin/python3
'''
from_json_string function
'''
import json


def from_json_string(my_str):
    '''
    function that returns an object represented by a JSON string

    Args:
        my_str: string

    Returns: Object represented by a json string
    '''
    return json.loads(my_str)
