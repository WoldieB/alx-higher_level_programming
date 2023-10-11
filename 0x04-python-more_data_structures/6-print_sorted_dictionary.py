#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_1 = list(a_dictionary.keys())
    list_1.sort()
    for i in list_1:
        print("{}: {}".format(i, a_dictionary.get(i)))
