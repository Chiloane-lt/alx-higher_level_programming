#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    hid_list = dir(hidden_4)
    for i in hid_list:
        if i[:2] != '__':
            print("{}".format(i))
