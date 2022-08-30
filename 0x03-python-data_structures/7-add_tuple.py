#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = len(tuple_a)
    b = len(tuple_b)

    mylist = []

    if a > 1 and b > 1:
        mylist.append(tuple_a[0] + tuple_b[0])
        mylist.append(tuple_a[1] + tuple_b[1])
    elif a == 1 and b == 1:
        mylist.append(tuple_a[0] + tuple_b[0])
        mylist.append(0 + 0)
    elif a == 1:
        mylist.append(tuple_a[0] + tuple_b[0])
        mylist.append(0 + tuple_b[1])
    elif a == 0 and b == 0:
        mylist.append(0 + 0)
        mylist.append(0 + 0)
    elif not tuple_a:
        mylist.append(0 + tuple_b[0])
        mylist.append(0 + tuple_b[1])
    elif b == 1:
        mylist.append(tuple_a[0] + tuple_b[0])
        mylist.append(tuple_a[1] + 0)
    elif not tuple_b:
        mylist.append(0 + tuple_a[0])
        mylist.append(0 + tuple_a[1])

    mytuple = tuple(mylist)
    return mytuple
