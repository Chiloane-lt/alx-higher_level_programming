#!/usr/bin/python3
for i in range(0, 10):
    for x in range (0, 10):
        if ((x != i) and (i < x)):
            if (i == 8 and 9 == 9):
                print("{}{}\n".format(i,x), end="")
            else:
                print("{}{}".format(i, x), end=", ")
