class Student:
    def __init__(self, sid, sname, smnrks):
        self.stud_roolno = sid
        self.stud_name = sname
        self.stud_marks = smnrks

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''\n{self.__dict__}'''


s1 = Student(101, 'Sham', 243)
for i in range(10):
    print(s1)
