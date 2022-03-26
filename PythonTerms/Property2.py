class Student:
    def __init__(self,rollno,name,marks):
        self.stud_rollno = rollno
        self.stud_name = name
        self.stud_marks = marks

    def __str__(self):
        return f'''Roll No:{self.stud_rollno}, Name:{self.stud_name}, Marks:{self.stud_marks}'''

    def __repr__(self):
        return str(self)

    def get_marks(self):
        if self.__dict__.__contains__('_stud_marks'):
            return self._stud_marks
        return ""

    def set_marks(self, marks):
        if type(marks) == float:
            if marks < 0.00:
                print("Invalid Marks")
            else:
                self._stud_marks =marks
        else:
            print('Invalid Data....')

    stud_marks = property(fget=get_marks, fset=set_marks)

s1 = Student(101,'Sham',23.45)
print(s1)
s1.stud_marks = -40.90
print(s1)
