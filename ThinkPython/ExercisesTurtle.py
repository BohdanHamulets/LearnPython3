#!/usr/bin/env python3


import turtle


bob = turtle.Turtle()

'''
def draw_square(t, _length):
    for x in range(4):
        bob.fd(_length)
        bob.lt(90)
    turtle.mainloop()


draw_square(bob, 200)
'''


def polygon(t, _length=10, n=60):
    angle = 360 / n
    for x in range(n):
        t.fd(_length)
        t.lt(angle)
    turtle.mainloop()


polygon(bob, 10)
