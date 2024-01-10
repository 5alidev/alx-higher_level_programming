#!/usr/bin/python3
def number_keys(a_dictionary):
    """returns the number of keys in a dictionary."""
    count = 0
    for k in a_dictionary.items():
        count += 1
    return count
