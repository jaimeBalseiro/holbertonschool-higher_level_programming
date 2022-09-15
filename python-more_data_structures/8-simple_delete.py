#!/usr/bin/pyhton3


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary['track']
    return a_dictionary
