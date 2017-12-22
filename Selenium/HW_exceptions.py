"""
HW 2
"""

class Car(object):

    def __init__(self):
        print("this starts the class, as I was told ^_^")

    def get_vendor(self):
        print("BMW")

    def get_model(self):
        print("550i")
    def get_year(self):
        print(2017)

try:
    my_car = Car()
    my_car.get_model()
    my_car.get_color()
except:
    print("smth went wrong. I don't know what, I'm just a machine")
    raise Exception("I'm letting ya' know") # comment this for nicer output... LOL!
finally:
    print("Code in here will always run")
