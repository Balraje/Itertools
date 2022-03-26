import random
class Student:
    def __init__(self,rollno,name):
        self.student_rollno = rollno
        self.student_name = name
        Student.count =Student.count+1

    def __str__(self):
        return f'\n{self.__dict__}'

    def __repr__(self):
        return str(self)

    count=1
    @classmethod
    def get_studnent_info(cls):
        return cls(rollno=round(random.randint(1,100)),
                   name='Ganesh'+str(Student.count)
                   )

studentList= []
for i in range(10):
    s=Student.get_studnent_info()
    studentList.append(s)
print(studentList)
