#!/usr/bin/python3
def safe_print_integer_err(value):
    """prints an integer."""
    import sys
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return False
