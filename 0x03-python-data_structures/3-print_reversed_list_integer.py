#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = (len(my_list) + 1) * (-1)
    if my_list is not None:
        for x in range(-1, a, -1):
            print("{:d}".format(my_list[x]))
    else:
        return None
