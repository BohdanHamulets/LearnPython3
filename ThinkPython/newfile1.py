#!/usr/bin/env python3

import time
import turtle

# some_text = input("What fo you want to print?\n")


def print_user(some_text):
    if len(some_text) > 0:
        print(">>> ", some_text)
    else:
        pass


# print_user(some_text)

def my_get_time():
    seconds = time.time()
    days = 60 * 60 * 24
    days_since_epoch = seconds // days
    rest_time = seconds % days
    rest_time_hours = rest_time / (60 * 60)
    _hours = rest_time_hours // 1
    _minutes = rest_time_hours % 1
    print(days_since_epoch, " days have past after 1 Jan 1970", _hours, "HOURS", _minutes, "MINUTES")


# my_get_time()

# a = input("Ready to check if you can get a triangle? Please input side a\n")
# b = input("Please input side b\n")
# c = input("Please input side c\n")


def triangle(a, b, c):
    if a > b + c or b > a + c or c > b + a:
        print("Nope, you cannot")
    else:
        print("Yes you can!")


# triangle(a, b, c)


def book_rec(n, s):
    if n == 0:
        print(s)
    else:
        print(n, s)
        book_rec(n - 1, n + s)


# book_rec(3, 0)


def draw(t, length, n):
    if n == 0:
        turtle.mainloop()
        return
    angle = 50
    t.fd(length * n)
    t.lt(angle)
    draw(t, length, n - 1)
    t.rt(2 * angle)
    draw(t, length, n - 1)
    t.lt(angle)
    t.bk(length * n)


bodja = turtle.Turtle()


# draw(bodja, 15, 3)


def return_function(x):
    if x < 0:
        return -x
    if x > 0:
        return x


# print(return_function(-5))


def zadacha(x, y):
    if x > y:
        return 1
    if x < y:
        return -1
    else:
        return 0


#print(zadacha(6, 5))


# квадрат гіпотенузи дорівнює сумі квадратів катедів
# 5 ** 2 == 4 ** 2 + 3 ** 2


def hypotunyza(a, b):
    #kvadrat_a = a ** 2
    #kvadrat_b = b ** 2
    #result = kvadrat_b + kvadrat_a
    return b ** 2 + a ** 2

# print(hypotunyza(7, 3))


def is_divisible( x , y ):
    return x % y == 0

# bla = is_divisible(3,3)
# print(bla)
# print("AAAAA")
# print(is_divisible(3,4))


def break_func(x):
    while x < 10:
        print("Doing smth, wail . . . ", x)
        x += 1
        if x == 9:
            break
            print("We just breaked")
        print("Smth else")

#break_func(1)


def advanced_wait(param):
    #if param > 3:
    #print("We found it")
    while param <= 4:
        print("We're looking for it")
        param += 1
        if param >= 4:
            print("It's bigger than 4")
            continue
            print("Is this like else or what?")


# advanced_wait(1)


def blaa():
    listt = []
    for x in range(3):
        print(x)
        listt.append(x)
    return listt
    print("bla")

# blaa()


def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod


def a (x, y):
    x = x + 1
    return x * y

b(5)