#!/usr/bin/env python3

# import math

"""
while True:
    x = input("> ")
    if x == "done":
        print("Ok, fine")
        break
    print(eval(x))
"""

#somestr = input("Write str > ")
#_number = len(somestr)

"""
while _number > 0:
    print(somestr[_number-1])
    _number = _number - 1
    print(_number)
"""


def find_something(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return "there isn't such letter"


# print(find_something("Marvel", "i"))

def count_letters(word, letter):
    number = 0
    for element in word:
        if element == letter:
            number += 1
    return "This letter in a given word appears " + str(number) + " times"


print(count_letters("Bohdan", "o"))

bla = "WORDL"

bla.find()








