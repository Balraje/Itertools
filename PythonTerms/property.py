class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('Getting name')
        return self._name

    def set_name(self, value):
        print('Setting name to ' + value)
        self._name = value

    def del_name(self):
        print('Deleting name')
        del self._name

    # Set property to use get_name, set_name
    # and del_name methods
    name = property(fget=get_name, fset=set_name, fdel=del_name,doc='Name property')

p = Person('Adam')
print(p.name)
p.name = 'John'
print(p.name)
del p.name

