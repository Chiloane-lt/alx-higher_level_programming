#!/usr/bin/python3
import hidden_4

hid_list = dir(hidden_4)
for i in hid_list:
    if i[:2] != '__':
        print("{}".format(i))
