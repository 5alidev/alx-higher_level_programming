#!/usr/bin/python3
def magic_calculation(a, b):
    add = magic_calculations_102.add
    sub = magic_calculations_102.sub
    if a < b:
        c = add(a, b)
        for n in range(4, 6):
            c = add(c, n)
        return c
    else:
        return sub(a, b)
