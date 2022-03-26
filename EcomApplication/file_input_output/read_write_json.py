import json
import random

cities =['Pune','Mumbai', 'Banglore','Hydrabad', 'Gurgaon', 'Delhi']

class Student:
    def __init__(self, rollno, sname, address, marks):
        self.student_rolllno = int(rollno)
        self.student_name = str(sname)
        self.student_address = str(address)
        self.student_marks = float(marks)
        Student.count = Student.count + 1

    def __str__(self):
        return f'''\n{self.__dict__}'''

    def __repr__(self):
        return str(self)

    count = 1

    @classmethod
    def get_student_info(cls):
        return cls(rollno = Student.count,
                   sname= 'Student' + str(Student.count),
                   address = cities[random.randint(0, len(cities)-1)],
                   marks = round(random.randint(1,600)/6, 2)
                   )

studList = []
for i in range(9):
    studList.append(Student.get_student_info())
print('------------------------------------------------------------------------------------------------------------')
print(studList)
print('------------------------------------------------------------------------------------------------------------')

file_path = "F:\\pythonProject\\EcomApplication\\file_input_output\\data_files\\"

def write_data_into_json(studList):
    with open(file_path+'Student.json','w') as file:
        file.write("[")
        for i in range(len(studList)):
            json_object = json.dumps(studList[i].__dict__, indent=2)
            file.write(json_object)
            if i != len(studList)-1:
                file.write(","+"\n")
        file.write("]")

    print("Student Data are added in Student.json file.....")

def read_data_from_json():
    #reading from file
    print("Read Data from Student.csv file.....")
    with open(file_path+'Student.json','r') as file:
        jsondict = json.load(file)
        print(jsondict)

#call function
write_data_into_json(studList)
read_data_from_json()






