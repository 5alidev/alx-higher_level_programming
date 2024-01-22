#!/usr/bin/python3
def safe_function(fct, *args):
    """function that executes a function safely."""
    import sys
    try:
        result = fct(*args)
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return None
    return result
