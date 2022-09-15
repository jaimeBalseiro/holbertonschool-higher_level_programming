#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    for k, v in sorted(a_dictionary.items()):
        print("{}: {}".format(k, v))
'''You can also use the "print(f"{}: {}") f-string that is easier and faster to read/ undestand'''
