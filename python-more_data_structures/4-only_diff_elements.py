#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    both_sets = list(set_1) + list(set_2)
    result = set()

    for item in both_sets:

        if (item in set_1) != (item in set_2):
            result.add(item)
            
    return result
