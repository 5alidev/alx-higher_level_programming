#!/usr/bin/python3
def best_score(a_dictionary):
    """returns a key with the biggest integer value."""
    if not a_dictionary:
        return None
    max_val = 0
    best_key = None
    for k, v in a_dictionary.items():
        if v > max_val:
            max_val = v
            best_key = k
    return best_key
