#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    First = 0

    if not len(sentence):
        first = None
    else:
        first = sentence[0]

    mytuple = (a, first)
    return mytuple
