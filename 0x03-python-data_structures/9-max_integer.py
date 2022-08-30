#!/usr/bin/python3
def max_integer(my_list=[]):

    maximum = 0
    a = len(my_list)

    if a == 0:
        return None
    else:
        maximum = my_list[0]
        for i in range(a):
            if maximum < my_list[i]:
                maximum = my_list[i]
        return maximum
