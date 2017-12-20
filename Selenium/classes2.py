"""         OOP
Object Oriented Programming
"""

class Car(object):

    def __init__(self):
        print("You've just created the car instance")

    def drive(self):
        print("The car is started, wruuum!")

    def stop(self):
        print("The car is stopping .... stopped!")

class BMW(Car):

    def __init__(self):
        Car.__init__(self)
        print("You've just created a BMW car")

    def turn(self):
        print("I don't need no truning light! I drive a B.M.W.")

    def drive(self):
        super().drive() # This feature we can use to first execute functionality of the parent class,\
        #  and that we're adding ours. super().<method_name>() - will do da ting!
        print("BMW says WRRRUUUMMM!!!! ")


kybik = BMW()

kybik.turn()
kybik.drive()
#print(dir(kybik))