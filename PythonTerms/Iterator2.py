class TimesOfIndia:
    def __init__(self,num):
        with open("F:\\pythonProject\\PythonTerms\\data_files\\NewPaper.txt",'r') as file:
            self.alllines = [line.strip() for line in file.readlines()]
            self.number_of_recordshow = num

    def __iter__(self):
        return self

    def __next__(self):
        if self.alllines:
            records = self.alllines[0:self.number_of_recordshow]
            self.alllines = self.alllines[self.number_of_recordshow::]
            return records[0]
        else:
            raise StopIteration('No Reocrds..')


toi = TimesOfIndia(1)
import time
for read in toi:
    print(read)
    if len(read)>100:
        time.sleep(2)
    elif len(read)<100and len (read)>50:
        time.sleep(1)
    else:
        time.sleep(0)


