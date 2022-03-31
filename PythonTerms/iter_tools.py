list1= [[1,2,3],[4,5,6],[7,8,9]]
list2= [[10,11,12],[13,14,15],[16,17,18]]
s=sum([num for elem in list1 for num in elem]+[num for elem in list2 for num in elem])
print(s)
print(s)