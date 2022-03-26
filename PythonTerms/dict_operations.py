#'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
color =	{"color1": "red","color2": "blue","color3": "green"}

print(color.copy()) #It is used to return a copy of the dictionary.

name = ('c1','c2','c3')
print(color.fromkeys(name,'RED')) #It is used to return a dictionary with the specified keys and value.

print(color.get('color2')) #It is used to return the value of the specified key.

print(color.items()) #It is used to return a list containing a tuple for each key value pair.

print(color.keys()) #It is used to return a list containing the dictionary's keys.

print(color.pop('color3'))#It is used to remove the element with the specified key.

print(color.setdefault('clr','WHITE')) #It is used to return the value of the specified key. If the key does not exist then insert the key, with the specified value.
print(color)

print(color.update({'clr':'Yellow','clrnew':'Orange'}))#It is used to update the dictionary with the specified key-value pairs.
print(color)

print(color.values())
print(color.popitem())

print(color.clear()) #It is used to removes all the elements from the dictionary.  --->None