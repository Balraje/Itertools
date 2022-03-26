from abc import ABC, abstractmethod
from student import Student_info
class StudentServices:
    @abstractmethod
    def add_student(self,stud:Student):
        pass

    @abstractmethod
    def find_sum_marks(self,rollno:int):
        pass