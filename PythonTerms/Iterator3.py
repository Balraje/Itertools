class Punyanagari:
    def __init__(self, num):
        with open('F:\\pythonProject\\PythonTerms\\data_files\\NewPaper.txt','r') as file:
            self.alllines = [line.strip() for line in file.readlines()]
            self.number_of_records_to_show = num

    def __iter__(self):
        return self

    def __next__(self):
        if self.alllines:
            record = self.alllines[0:self.number_of_records_to_show:]
            self.alllines =self.alllines[self.number_of_records_to_show::]
            return record[0]
        else:
            raise StopIteration('No Reocrds..')

p =Punyanagari(1)
import time

for read in p:
    print(read)
    if len(read)>100:
        time.sleep(2.5)
    if len(read)>50 and len(read)<100:
        time.sleep(1)
    if len(read) == 0:
        time.sleep(0)
    else:
        time.sleep(0)
