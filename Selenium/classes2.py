"""         OOP
Object Oriented Programming
"""

class Car(object):

    def __init__(self):
        print("You've just created the car instance")

    def drive(self):
        print("The car is starter, wruuum!")

    def stop(self):
        print("The car is stopping .... stopped!")

class BMW(Car):

    def __init__(self):
        Car.__init__(self)
        print("You've just created a BMW car")

    def turn(self):
        print("I don't need no truning light! I drive a B.M.W.")

    def drive(self):
        print("BMW says WRRRUUUMMM!!!! ")


kybik = BMW()

kybik.turn()
kybik.drive()