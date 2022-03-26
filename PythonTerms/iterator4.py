class IteratorDemo:
    def __init__(self, value):
        self.value =value
        self.lst = [10,20,30,40]

    def __iter__(self):
        return self

    def __next__(self):
        if self.lst:
            record = self.lst[0:self.value:]
            self.lst = self.lst[self.value::]
            return record[0]
        else:
            raise StopIteration('Record Not found')

obj = IteratorDemo(1)
for i in obj:
    print(i)
