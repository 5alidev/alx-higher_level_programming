#!/usr/bin/env python3
def no_c(my_string):
    new_str = ""
    for char in my_string:
        if char is not "C" and char is not "c":
            new_str += char
    return new_str
