#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbers = set()
    for number in my_list:
        unique_numbers.add(number)
        total_sum = sum(unique_numbers)

    return total_sum
