#!/usr/bin/python3

def islower(c):
    if (96 < ord(c) < 123):
        return True
    else:
        return False

def uppercase(str):
    for i in range(0, len(str)):
        if islower(str[i]):
            print(chr(ord(str[i]) - 32), end="")
        else:
            print(str[i], end="")
    print()
