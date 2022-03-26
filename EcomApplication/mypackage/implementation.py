from services import StudentServices, Student_info
class StudentImplementation:
    studentlist= []
    def add_student(self, stud: Student):
        r= int(input("Enter Roll No:"))
        name= input("Enter the Roll No:")
        marks= input("Enter the Marks")
        self.studentlist.append(r, name, marks)


