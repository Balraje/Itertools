class Person:
    def __init__(self,pname,age):
        self.person_name = pname
        self. perosn_age = age

    def __str__(self):
        return f'''Person Name: {self.person_name}, Person Age:{self.perosn_age}'''

    def __repr__(self):
        return str(self)

    def get_age(self):
        if self.__dict__.__contains__('_person_age'):
            return self._perosn_age
        return ""
    def set_age(self,age):
        if type(age) == int:
            if age<0:
                print('Invalid Age')
            else:
                self.perosn_age = age
        else:
            print("Invalid Data..")


    person_age = property(fget=get_age, fset=set_age)

p1= Person('Sham',-23)
print(p1)
p1.person_age = 32
print(p1)
