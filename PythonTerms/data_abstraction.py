from abc import ABC
class Car(ABC):
    def mileage(self):
        pass

class Suzuki(Car):
    def mileage(self):
        print("The mileage is 30KM/L")

class Honda(Car):
    def mileage(self):
        print("THe mileage is 25 KM/L")

class Toyato(Car):
    def mileage(self):
        print("The mileage is 20 KM/L")

s=Suzuki()
s.mileage()

h= Honda()
h.mileage()

t=Toyato()
t.mileage()

