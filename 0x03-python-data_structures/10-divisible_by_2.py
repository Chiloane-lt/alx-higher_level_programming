#!/usr/bin/python3
def divisible_by_2(my_list=[]):
#    nulist = []

#    for i in my_list:
#        if (my_list[i] % 2) == 0:
#            nulist.append(True)
#        else:
#            nulist.append(False)
#    return nulist

    nulist = [True if my_list[i] % 2 == 0 else False for i in my_list]
    return nulist
