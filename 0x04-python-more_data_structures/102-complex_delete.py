#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key = list(a_dictionary.keys())

    for value_1 in key:
        if value == a_dictionary.get(value_1):
            del a_dictionary[value_1]

    return (a_dictionary)
