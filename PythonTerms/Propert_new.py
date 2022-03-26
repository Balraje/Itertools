class Ganesh:
    def __init__(self,age):
        self.ganesh_age =age

    def get_age(self):
        return self._ganesh_age

    def set_age(self,value):
        if type(value) == int:
            if value<=0:
                print("Invalid Age")
            else:
                self._ganesh_age = value
        else:
            print('Invalid Data')

    ganesh_age =property(fget=get_age,fset=set_age)

g = Ganesh(30)
print(g.ganesh_age)

g.ganesh_age =-30
print(g.ganesh_age)
