def magic_calculation(a, b):
    add, sub = magic_calculation_102.add, magic_calculation_102.sub

    if a < b:
        c = add(a, b)
        for n in range(4, 6):
            c = add(c, n)
        return c
    else:
        return sub(a, b)
