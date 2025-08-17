class Car:
    total_cars = 0  

    def __init__(self, make, model):  
        self.make = make
        self.model = model
        Car.total_cars += 1  

    def display_car(self):
        return self.make + " " + self.model

    @staticmethod
    def get_total_cars():
        return Car.total_cars


c1 = Car("Toyota", "Corolla")
c2 = Car("Honda", "Civic")

print(c1.display_car())
print(c2.display_car())
print("Total cars created:", Car.get_total_cars())