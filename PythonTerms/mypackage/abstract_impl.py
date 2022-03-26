from mypackage.abstract_demo import Car
class Impl(Car):
    def mileage(self):
        print('The mileage is 30 Km/l')

obj =Impl()
obj.mileage()
