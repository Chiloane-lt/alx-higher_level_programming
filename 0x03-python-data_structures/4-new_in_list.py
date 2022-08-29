#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a = len(my_list)
    copy = list(my_list)

    if (idx < 0):
        return copy
    elif idx > a:
        return copy
    else:
        copy[idx] = element
        return copy
