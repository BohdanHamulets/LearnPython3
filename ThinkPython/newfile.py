#!/usr/bin/env python3


def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    seredyna = word[1:-1]
    for x in range(int(len(seredyna))):
        print(seredyna[x])

    return word[1:-1]


"""
print(first("Bohdan"))
print(last("Bohdan"))
print(middle("Bohdan"))
"""

middle("Bohdan")