#!/usr/bin/python3
def no_c(my_string):
    removal = {99 : None, 67 : None}
    nu_str = my_string.translate(removal)
    return nu_str
