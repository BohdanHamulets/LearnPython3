"""         OOP
Object Oriented Programming
"""


class Car(object):
    wheels = 4

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_info(self):
        print("Car brand is", self.brand, "\n", "Car model is", self.model)

    def change_wheels(self, new_val):
        self.wheels = new_val
        print("Number of wheels is", new_val)

if __name__ == "__main__":
    print(Car.wheels)

    first_new_car = Car("bmw", "550i")
    first_new_car.wheels = 8

    inherited_car = first_new_car
    print("this is inherited car - ", inherited_car.wheels)


    def some_funk():
        print("bla")

    some_funk()
