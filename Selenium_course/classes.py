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


print(Car.wheels)

first_new_car = Car("bmw", "550i")
first_new_car.wheels = 8

inherited_car = first_new_car
print("this is inherited car - ", inherited_car.wheels)

print(first_new_car.wheels)

first_new_car.get_info()

# print(first_new_car.brand, first_new_car.model)