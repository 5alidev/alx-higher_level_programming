#!/usr/bin/env python3
def no_c(my_string):
    new_str = ""
    for c in my_string:
        if c is not 'C' and c is not 'c':
            new_str += c
    return new_str
