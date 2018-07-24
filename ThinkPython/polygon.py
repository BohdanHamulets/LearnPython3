"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import math
import turtle


def square(t, length):
    """Draws a square with sides of the given length.

    Returns the Turtle to the starting position and location.
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    print("this is print 1 of polyline function which decides how many steps should be taken, steps: ", n)
    print("this is print 2 of polyline function, it's got length: ", length, "and angle: ", angle)
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    """Draws a polygon with n sides.

    t: Turtle
    n: number of sides
    length: length of each side.
    """
    print("this is a polygon function, I don't now how but it has a value n which is used to calculate angle, n: ", n)
    angle = 360.0/n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """

    arc_length = 2 * math.pi * r * abs(angle) / 360
    print("This is arc function print 1,", " value for arc_length is: ", arc_length)
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    print("This is arc function print 2,", " value for step_length is: ", step_length)
    step_angle = float(angle) / n
    print("This is arc function print 3,", " value for step_angle is: ", step_angle, "kyt dla \n",
    "turtle stanovutume / 2")
    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)

    polyline(t, n, step_length, step_angle)
    print("This is a arc function print 5, it calls polyline function with n, step_length, step_angle: ", n, step_length, step_angle)
    t.rt(step_angle/2)


def circle(t, r):
    """Draws a circle with the given radius.

    t: Turtle
    r: radius
    """
    print("This is circle print, values are: ", "given_radius: ", r, "Turtle: ", t)
    arc(t, r, 360)


# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':
    bob = turtle.Turtle()

    # draw a circle centered on the origin
    radius = 200
    bob.pu()
    bob.fd(radius)
    bob.lt(90)
    bob.pd()
    circle(bob, radius)

    # wait for the user to close the window
    turtle.mainloop()
