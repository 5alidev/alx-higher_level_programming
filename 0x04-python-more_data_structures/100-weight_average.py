#!/usr/bin/python3
def weight_average(my_list=[]):
    """weighted average of all integers tuple"""
    avg = 0
    n = 0
    if len(my_list) <= 0:
        return 0
    for i, tup in enumerate(my_list):
        avg += (my_list[i][0] * my_list[i][1])
        n += my_list[i][1]
    return avg / n
