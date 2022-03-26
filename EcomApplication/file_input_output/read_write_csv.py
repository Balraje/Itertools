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

def write_data_into_csv(studList):
    datalines =[]
    for stud in studList:
        datastr = str(stud.student_rolllno)+"," + stud.student_name + "," + stud.student_address+","+str(stud.student_marks)+"\n"
        datalines.append(datastr)

    with open(file_path + 'Student.csv','w') as file:
        for lines in datalines:
            file.writelines(lines)
    print("Student Data are added in Student.csv file.....")

def read_data_from_csv():
    #reading from file
    print("Read Data from Student.csv file.....")
    slist = []
    print('Reading Data from file')
    with open(file_path + 'Student.csv', 'r') as file:
        alllines = [line.strip() for line in file.readlines()]
        #print(alllines)

        for line in alllines:
            words = line.split(',')
            slist.append(Student(rollno=words[0], sname= words[1], address= words[2],marks = words[3]))
        print(slist )

#call function
write_data_into_csv(studList)
read_data_from_csv()