from collections import *
import random
import sys
#UserString
class MyString(UserString):
    #function to append to string
    def append(self,s):
        self.data += s

    #function to remove from the string
    def remove(self,s):
        self.data=self.data.replace(s,"")

s1= MyString('Hello')
print('Original String',s1.data)

#Appending to string
s1.append("s")
print('String After Appending:',s1.data)

#removing from the string
s1.remove('e')
print('String After Removing',s1.data)

sys.exit(0)

class MyList(UserList):
    def remove(self, item:None) -> None:
        raise RuntimeError('Deletion Not Allowed')

    def pop(self, item =None):
        raise RuntimeError('Deletion Not allowed')

l=MyList([1,2,3,4,5])
print('Original List:',l)

#inserting to list
l.append(6)
print('After Insertion:',l)

#deleting from list
l.remove(3)

sys.exit(0)
#UserDict
class MyDict(UserDict):
    #stop deletion from the dict
    def __del__(self):
        raise RuntimeError('Deletion from dict Not Allowed')

    #stop to pop element from dict
    def pop(self, s=None):
        raise RuntimeError('Deletion from dict Not Allowed')

    #stop to popinter from dict
    def popitem(self,s=None):
        raise RuntimeError('Deletion from dict Not Allowed')

m=MyDict({'a':1,'b':2,'c':3})
m.pop(1)


sys.exit(0)
#DefaultDict
l=[1,2,3,4,2,4,1,2]
d=defaultdict(int)
for i in l:
    d[i]+=1


sys.exit(0)
#OrderedDict
d={}
d['a']=1
d['b']=2
d['c']=3
d['d']=4
print('Normal Dict.....')
for key,value in d.items():
    print(key,value,end=',')  #a 1,b 2,c 3,d 4,
od = OrderedDict()
od['a']=1
od['b']=2
od['c']=3
od['d']=4
print('\nOrdered Dict...Before updation')
for key,value in od.items():
    print(key,value,end=',')      #a 1,b 2,c 3,d 4,

print('\nOrdered Dict...After updation')
od['c']=5
for key,value in od.items():
    print(key,value,end=',')  #a 1,b 2,c 5,d 4,

print('\nOrdered Dict...After Deletion')
od.pop('c')
for key,value in od.items():
    print(key,value,end=',') #a 1,b 2,d 4,

print('\nOrdered Dict...After Re-insertion')
od['c'] =3
for key,value in od.items():
    print(key,value,end=',')  #a 1,b 2,d 4,c 3,


sys.exit(0)



#Counter object
c= Counter()  #empty counter object
print(c)
c=Counter('Mumbai') #a new Counter from an iterable
print(c)
c=Counter({'a':1,'b':2}) #a new Counter from mappings
print(c)
c=Counter(cats=4,dogs=8) # a new counter from keyword args
print(c)
print(c['asdasdasd'])  # count of a missing element is zero

c=Counter(a=4,b=2,c=0,d=-2)

# Return an iterator over elements repeating each as many times as its count
#If an element’s count is less than one, elements() will ignore it.
print(sorted(c.elements()))

#Return a list of the n most common elements and their counts from the most common to the least
print(Counter('abracadabra').most_common(3))


#substract
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print(c)


#total--->  Compute the sum of the counts.
c = Counter(a=4, b=2, c=0, d=-2)
s= c.total()
print(s)

sys.exit(0)
#ChainMap implementation
d1={"color1": "red","color2": "blue","color3": "green"}
d2={'c1':'Pink','c2':'orange'}



# Defining the chainmap
cm = ChainMap(d1, d2)
print(cm)

# Accessing Values using key name
print(cm['c2'])  #orange

# Accessing values using values() method
print(cm.values())

# Accessing keys using keys() method
print(cm.keys())

d3={'c3':'Violet','c4':'Purple'}

#using new_child() to add new dictionary
cm1= cm.new_child(d3)
print(cm1)

#display parents
print(cm1.parents)



sys.exit(0)
#deque implemntation of all methods

dq= deque([1,2,3,4],maxlen=100)
print(dq)
dq.append(5)
print(dq)
dq.appendleft(55)
print(dq)
d=dq.copy()
print(d)
n= dq.count(55)
print(n)
dq.extend(d)
print(dq)
dq.extendleft([11,22,33])
print(dq)
print(dq.index(11,1,5))
dq.insert(3,333)
print(dq)
print(dq.pop())
print(dq.popleft())
dq.remove(333)
print(dq)
dq.reverse()
print(dq)
dq.rotate(2)
print(dq)

sys.exit(0)
#Declaring namedtuple
Employee = namedtuple('Employee',['name','age','address'])
#adding values
e=Employee('Sagar','23','Solapur')
#access using index
print('The address of employee:',e[2])
#access using name
print('The Age of employee:',e.age)




sys.exit(0)
elements = [9, 29, 2, 1, 20, 3, 25, 29, 18, 6, 12, 28, 13, 5, 2, 15, 17, 22, 6, 6, 30, 23, 5, 28, 12, 1, 2, 8, 14, 21, 16, 21, 23, 10, 22, 15, 23, 17, 26, 14, 4, 30, 20, 24, 5, 24, 2, 7, 3, 1, 26, 20, 11, 26, 24, 26, 20, 25, 30, 30, 8, 25, 9, 30, 5, 23, 19, 10, 19, 20, 25, 18, 3, 17, 27, 19, 24, 9, 29, 29, 27, 29, 19, 17, 19, 12, 27, 7, 6, 9, 10, 20, 25, 26, 10, 23, 30, 1, 12, 6]
contr = Counter(elements)
print(contr)


for item in set(elements):
    print(item,elements.count(item))