# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint',
# 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

s1 = {1,2,3,4,5}
s2 = {11,12,3,4,15}
#add It is used to add an element to the set.
s1.add(6)
print(s1)
s1.clear()
print(s1)

#copy It is used to return a copy of the set.
newset = s1.copy()
print(s1,id(s1))  #{1, 2, 3, 4, 5} 958097732768
print(newset,id(newset))  #{1, 2, 3, 4, 5} 958100838880

#'difference' It is used to return a set containing the difference between two or more sets.
x = {"Abhi", "Jerry", "Mickey"}
y = {"Wings", "Alpha", "Jerry"}
z = {'Abhi'}
print(x.difference(y))
print(x.difference(y,z))

#'difference_update' It is used to remove the items in this set that are also included in another specified set.
x = {"Abhi", "Jerry", "Mickey"}
y = {"Wings", "Alpha", "Jerry"}
x.difference_update(y)
print(x)

#discard It is used to remove the specified item.
y.discard('Alpha')
print(y)

#'intersection' t is used to return a set that is the intersection of two other sets.
x = {"Abhi", "Jerry", "Mickey"}
y = {"Wings", "Alpha", "Jerry"}

newset = x.intersection(y)
print(newset)

#'intersection_update' t is used to remove the items in this set that are not present in other specified set.
x.intersection_update(y)
print(x)

#'isdisjoint' It is used to return whether two sets have a intersection or not.
x = {1,2,3,4,5}
y = {6,7,8,9}
print(x.isdisjoint(y)) #True

# 'issubset' 	It is used to return whether another set contains this set or not.
x = {11,2,3,4,1, 5}
y = {2,3}
print(y.issubset(x))

#'issuperset'  It is used to return whether this set contains another set or not.
print(x.issuperset(y))

#'pop' It is used to remove an element from the set.
x.pop()
print(x)

#'remove'  It is used to remove the specified element in the set.
x.remove(11)
print(x)

#'symmetric_difference' It is used to return a set with the symmetric differences of two sets.
print(x)
print(y)
print(x.symmetric_difference(y))

#'symmetric_difference_update' It is used to insert the symmetric differences from this set and another.
print(x)
print(y)
x.symmetric_difference_update(y)
print(x)

#union' It is used to return a set containing the union of sets.
x = {1,2,3,4,5}
y = {6,7,8,9}
print(x.union(y))

#'update' It is used to update the set with the union of this set and others.
print(x)
print(y)
x.update(y)
print(x)



