#!/usr/bin/python3
for i in reversed(range(97, 123)):
    if i % 2 == 0:
        print(f"{i:c}", end="")
    else:
        i = i - 32
        print(f"{i:c}", end="")
