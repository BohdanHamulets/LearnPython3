#!/usr/bin/env python3


def has_no_e():
    fin = open("words.txt")
    count_e = 0
    no_e = 0
    for line in fin:
        strip_word = line.strip()
        if 'e' not in line:
            no_e += 1
        else:
            count_e += 1
    print("total words = ", int(count_e) + int(no_e), "non e ", no_e)


has_no_e()


