#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0

    for w in range(x):
        try:
            print("{}".format(my_list[w]), end='')
        except:
            break
        else:
            c += 1

    print()
    return (c)
