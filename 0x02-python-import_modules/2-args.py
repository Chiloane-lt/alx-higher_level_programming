#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    list_args = list(sys.argv)
    num_args = len(list_args)
    num_input = num_args - 1

    if num_args < 2:
        print("{} arguments.".format(num_input))
    elif num_args == 2:
        print("{} argument:".format(num_input))
    else:
        print("{} arguments:".format(num_input))

    for i in range(1, num_args):
        print("{}: {}".format(i, list_args[i]))
