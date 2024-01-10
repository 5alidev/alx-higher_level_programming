#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """ replaces all occurrences of an element by another in a new list."""
    new_arr = []
    for elem in my_list:
        if elem is not search:
            new_arr.append(elem)
        else:
            new_arr.append(replace)
    return new_arr
