#!/usr/bin/python3
def uniq_add(my_list=[]):
    """adds all unique integers in a list"""
    uniq = list(set(my_list))
    sum = 0
    for e in uniq:
        sum += e
    return sum
