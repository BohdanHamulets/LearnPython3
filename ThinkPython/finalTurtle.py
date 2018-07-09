#!/usr/bin/env python3


import turtle

bob = turtle.Turtle()


def polygon(t, n=60, _length=170, angle=80):
    """This function draws a polygon using python turtle module
    Draws n lines segment with given length and angle, t is for turtle object
    """
    for x in range(n):
        t.fd(_length)
        t.lt(angle)
    turtle.mainloop()  # this is for the window to wait until closed


#polygon(bob, n=50, _length=65, angle=70)

polygon(bob)