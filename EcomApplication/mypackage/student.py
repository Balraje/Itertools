class Student_info:
    def __init__(self,rollno,sname,marks):
        self.studentRollno = rollno
        self. studentName = sname
        self. srudentMarks = marks

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''\n {self.__dict__}\n'''