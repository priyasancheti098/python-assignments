
class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Driving on the road")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the road")

c = Car()
b = Bicycle()

c.move()
b.move()
