#adding Property-----Property used to add business contstraints
class Employee:
    def __init__(self, eid, ename, age):
        self.emp_id = eid
        self.emp_name = ename
        self.emp_age = age


    def __str__(self):
        return f'''ID: {self.emp_id},Name: {self.emp_name},Age: {self.emp_age}'''


    def __repr__(self):
        return str(self)

    def get_age(self):
        if self.__dict__.__contains__('_emp_age'):
            return self._emp_age
        return ""

    def set_age(self, age):
        if type(age) == int:
            if age < 0:
                print("Invalid Age")
            else:
                self._emp_age = age
        else:
            print('Invalid Data....')

    emp_age = property(fget=get_age,fset=set_age)

e1 = Employee(101, 'asdad', 23)
print(e1)
e1.emp_age = 'sdfdsf'
print(e1)