#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """returns a new dictionary with all values multiplied by 2"""
    new_dict = a_dictionary.copy()
    for k in new_dict.keys():
        new_dict[k] *= 2
    return new_dict
