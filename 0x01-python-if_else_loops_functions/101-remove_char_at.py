#!/usr/bin/python3
# Author - Benhamou Khalid

def remove_char_at(str, n):
    """copy of string, removing the character at the position n"""
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
