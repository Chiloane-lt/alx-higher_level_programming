#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    args_list = list(sys.argv)
    num_args = len(sys.argv)

    if num_args == 4:
        a = int(args_list[1])
        b = int(args_list[3])

        if args_list[2] == '+':
            res = add(a, b)
            print("{} + {} = {}".format(a, b, res))
            sys.exit(0)
        elif args_list[2] == '-':
            res = sub(a, b)
            print("{} - {} = {}".format(a, b, res))
            sys.exit(0)
        elif args_list[2] == '*':
            res = mul(a, b)
            print("{} * {} = {}".format(a, b, res))
            sys.exit(0)
        elif args_list[2] == '/':
            res = div(a, b)
            print("{} / {} = {}".format(a, b, res))
            sys.exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
