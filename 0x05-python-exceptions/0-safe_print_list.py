#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """prints x elements of a list."""
    count = 0
    for i, value in enumerate(my_list):
        try:
            if i < x:
                print("{}".format(my_list[i]), end="")
                count += 1
        except IndexError:
            pass
    print()
    return count
