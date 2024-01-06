#!/usr/bin/env python3
def no_c(my_string):
    new_str = ""
    if my_string:
        for char in my_string:
            if char != "C" and char != "c":
                new_str += char
    return new_str
