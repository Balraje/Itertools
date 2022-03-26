import sys

list1= [[1,2,3],[4,5,6],[7,8,9]]
list2= [[10,11,12],[13,14,15],[16,17,18]]
s=sum([num for elem in list1 for num in elem]+[num for elem in list2 for num in elem])
print(s)

sys.exit(0)

s= list(map(lambda x:x**2,range(10)))
print(s)


sys.exit()

#shallow copy: modification in one can make in another
import copy
new = [[1,1,1],[2,2,2],[3,3,3]]
old = copy.copy(new)
new[1][1] = 11
print(new) #[[1, 1, 1], [2, 11, 2], [3, 3, 3]]
print(old) # [[1, 1, 1], [2, 11, 2], [3, 3, 3]]

#deep copy: modification in one cannot make in another
new = [[1,1,1],[2,2,2],[3,3,3]]
old = copy.deepcopy(new)
new[1][1] = 11
print(new) #[[1, 1, 1], [2, 11, 2], [3, 3, 3]]
print(old) #[[1, 1, 1], [2, 2, 2], [3, 3, 3]]


sys.exit(0)
import sys
from collections_object import deque

# 1 way
squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 2 way
sqr = list(map(lambda x: x ** 2, range(10)))
print(sqr)

# 3 way
sqrs = [x ** 2 for x in range(10)]
print(sqrs)

# this listcomp combines the elements of two lists if they are not equal:
listvalues = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(listvalues)    # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

#is equivalent to:
comb = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            comb.append((x,y))
print(comb)          #[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

vec = [-4,-2,0,2,4]
# create a new list with the values doubled
newlist = [x*2 for x in vec]
print(newlist)  #[-8, -4, 0, 4, 8]
# filter the list to exclude negative numbers
newlist = [x for x in vec if x>=0]
print(newlist)
# apply a function to all the elements
newlist = [abs(x) for x in vec]
print(newlist)

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
freshfruit=[weapon.strip() for weapon in freshfruit]
print(freshfruit)  #['banana', 'loganberry', 'passion fruit']

# create a list of 2-tuples like (number, square)
newlist = [(x,x**2) for x in range(6)]
print(newlist)  #[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3],[4,5,6],[7,8,9]]
newlist = [num for ele in vec for num in ele]
print(newlist)


#List comprehensions can contain complex expressions and nested functions:
from math import pi
newlist = [str(round(pi,i)) for i in range(1,6)]
print(newlist)


#Nested List Comprehensions
#Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length 4:
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
#The following list comprehension will transpose rows and columns:
newlist = [[row[i] for row in matrix] for i in range(4)]
print(newlist) #[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

#is equivalent to
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed) #[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

#In the real world, you should prefer built-in functions to complex flow statements.
# The zip() function would do a great job for this use case:
transposed = list(zip(*matrix))
print(transposed) #[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

# the del statement
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a) #[1, 66.25, 333, 333, 1234.5]
del a[2:4] #[1, 66.25, 1234.5]
print(a)
del a[:]
print(a) #[]
#del can also be used to delete entire variables:
del a
#print(a) #NameError: name 'a' is not defined

sys.exit(0)
queue = deque(['sam', 'merry', 'john'])
queue.append('Terry')
queue.append('Ram')
print(queue)
queue.popleft()
queue.popleft()
print(queue)

sys.exit(0)

# append', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort', 'clear'

list1 = [10, 20, 30, 40, 50]
list2 = [60, 70, 80]

print('Elements of List 1:', list1)
print('Elements of List 2:', list2)

# append
list1.append(55)
print('After appending 55 in list 1:', list1)  # [10, 20, 30, 40, 50, 55]
list1[len(list1):] = [55]
print(list1)

# copy
newlist = list1.copy()
print('After Copying in newlist:', newlist)  # After Copying in newlist: [10, 20, 30, 40, 50, 55]

# count

cnt = list1.count(20)
print('No. of times 20 in list1:', cnt)  # No. of times 20 in list1: 1

# extend
list1.extend(list2)
print('After extending list1 with list2',
      list1)  # After extending list1 with list2 [10, 20, 30, 40, 50, 55, 60, 70, 80]
list1[len(list1):] = list2
print(list1)

# index
idx = list1.index(55)
print('Index of 55 in list1:', idx)  # Index of 55 in list1: 5

# insert
list1.insert(2, 25)
print('25 inserted in list1 at index 2',
      list1)  # 25 inserted in list1 at index 2 [10, 20, 25, 30, 40, 50, 55, 60, 70, 80]
list1.insert(0, 25)
print(list1)
list1.insert(len(list1), 25)
print(list1)
list1.append(25)
print(list1)

# pop
list1.pop()
print('pop will delete the last element from list1:',
      list1)  # pop will delete the last element from list1: [10, 20, 25, 30, 40, 50, 55, 60, 70]

# pop(index)
list1.pop(2)
print('pop(index) will delete element at index 2 in list1:',
      list1)  # pop(index) will delete element at index 2 in list1: [10, 20, 30, 40, 50, 55, 60, 70]

# remove
list1.remove(10)
print("Remove will delete element 10 from list1",
      list1)  # Remove will delete element 10 from list1 [20, 30, 40, 50, 55, 60, 70]

# reverse
list1.reverse()
print('Reverse will reverse all the element from list1',
      list1)  # Reverse will reverse all the element from list1 [70, 60, 55, 50, 40, 30, 20]

# sort
list1.sort()
print('sort will sort all the element of list in acending order:',
      list1)  # sort will sort all the element of list in acending order: [20, 30, 40, 50, 55, 60, 70]

# clear
list1.clear()
print('clear method removers all element from the list and return empty list:',
      list1)  # clear method removers all element from the list and return empty list: []
del list1[:]
print(list1)

del list1  # delete the list1
# print(list1)  #NameError: name 'list1' is not defined


import sys
sys.exit(0)
#shallow copy: modification in one can make in another
l1=[1,2,3,4,5]
print(id(l1))
l2=l1.copy()
print(id(l2))

