class Person:
    def __init__(self,age):
        self.person_age=age

    def get_age(self):
        return self._person_age

    def set_age(self,value):
        if type(value) == int:
            if value<=0:
                raise ValueError('Invlaid Age...Must be Abovve zero')
            else:
                self._person_age = value
        else:
            print('Invalid Data')

    person_age =property(fget=get_age,fset=set_age)

p = Person(23)
print(p.person_age)
p.person_age = 24
print(p.person_age)
