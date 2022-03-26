import sys
value='Hello'
iter_obj = iter(value)
while True:
    try:
        item = next(iter_obj)
        print(item)
    except StopIteration:
        break

sys.exit(0)

class DataReader:
    def __init__(self, num):
        with open("F:\\pythonProject\\PythonTerms\\data_files\\NewPaper.txt", 'r') as file:
            self.alllines = [line.strip() for line in file.readlines()]
            self.no_of_records_to_show = num

    def __iter__(self):
        return  self

    def __next__(self):
        if self.alllines:
            records =  self.alllines[0:self.no_of_records_to_show:]
            self.alllines = self.alllines[self.no_of_records_to_show::]
            return records[0]
        else:
            raise  StopIteration("No Records")



d = DataReader(2)
import time
for read in d:
    time.sleep(1)
    print(read)
