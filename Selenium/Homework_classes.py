import random

class Fruit(object):
    def __init__(self):
        print("Fruit class started")
    def nutrition(self):
        bla = random.random()
        if bla <= 0.33:
            print("One third of the day dose")
        elif bla <= 0.66:
            print("Two third of the day dose")
        else:
            print("That's the whole day dose, be careful!")
    def fruit_shape(self):
        print("Shape is round")

class Apple(Fruit):
    def __init__(self):
        print("You've created apple, feel like god yet?")
    def nutrition(self):
        super().nutrition()
        print("You may just try it....I hope it'll be alright... ")
    def color(self, choice=None):
        self.choose = choice
        if choice is not None :
            print("Your choice of color is {color}".format(color=choice))
        else:
            pass

general_fruit = Fruit()
general_fruit.nutrition()
print("x"*30)
red_apple = Apple()
red_apple.nutrition()
red_apple.color("orange")
red_apple.fruit_shape()

