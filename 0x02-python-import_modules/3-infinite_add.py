#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    list_args = list(sys.argv)
    num_args = len(list_args)

    total = 0

    for i in range(1, num_args):
        total = total + int(list_args[i])

    print("{}".format(int(total)))
