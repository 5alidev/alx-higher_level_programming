#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """prints the first x elements of a list and only integers."""
    count = 0
    for i, value in enumerate(my_list):
        try:
            if i < x:
                print("{:d}".format(my_list[i]), end = "")
                count += 1
        except (ValueError, TypeError):
            pass
        print()
        return count
