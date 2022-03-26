

string_methods = ('capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map',\
                  'index', 'isalnum','isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', \
                  'isprintable', 'isspace', 'istitle', 'isupper', 'join','ljust', 'lower', 'lstrip', 'maketrans', 'partition', \
                  'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition','rsplit', 'rstrip', 'split', \
                  'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill')
number_of_methods = len(string_methods)
print(number_of_methods)


str = 'hello welcome to Python String Operations'
print(str.capitalize()) #It is used to convert the first character to upper case.
print(str.casefold()) #It is used to convert string into lower case.
print(str.center(100,'*')) #It is used to return a centered string.
print(str.count('e')) #It is used to return the number of times a specified value occurs in a string.

txt = "Welocme to \ $ Python "
#It is used to return an encoded version of the string.
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

print(str.endswith('hello')) #It is used to return true if the string ends with the specified value.
print(str.expandtabs(10)) #It is used to set the tab size of the string.

print(str.find('come'))#It is used to search the string for a specified value and return the position of where it was found.

a=10
b=20
print('a={} and b={}'.format(a,b)) #It is used to format specified values in a string.

a = {'x':'Jerry', 'y':'Stark'}
print("{x}'s last name is {y}".format_map(a)) #It is used to format specified values in a string.

print(str.index('e')) #It is used to search the string for a specified value and return the position of where it was found.

str = 'Welocme to Python 123 Programming'
print(str.isalnum()) #It is used to

print(str.isalpha()) #It is used to return True if all characters in the string are in the alphabet.
print(str.isdecimal()) #It is used to return True if all characters in the string are decimals.
print(str.isdigit()) #It is used to return True if all characters in the string are digits.
print(str.isidentifier()) #It is used to return True if the string is an identifier.
print(str.islower()) #It is used to return True if all characters in the string are lower case.
print(str.isnumeric()) #It is used to return True if all characters in the string are numeric.
print(str.isprintable()) #It is used to return True if all characters in the string are printable.
print(str.isspace()) #It is used to return True if all characters in the string are whitespaces.
print(str.istitle()) #It is used to return True if the string follows the rules of a title.
print(str.isupper()) #It is used to return True if all characters in the string are upper case.
print(str.join(['E'])) #	It is used to Join the elements of an iterable to the end of the string.
print(str.ljust(10,'x')) #It is used to return a left justified version of the string.
print((str.lower())) #It is used to convert a string into lower case.
#print(str.maketrans()) #It is used to return a translation table to be used in translations.
print(str.partition('sad')) #It is used to return a tuple where the string is parted into three parts.
print(str.replace('e','X')) #It is used to return a string where a specified value is replaced with a specified value.
print(str.rfind('to')) #It is used to search the string for a specified value and return the last position of where it was found.
print(str.rindex('to')) #It is used to search the string for a specified value and return the last position of where it was found.
print(str.rjust(1)) #It is used to return a right justified version of the string.
print(str.rpartition('asd'))#It is used to return a tuple where the string is parted into three parts.
print(str.rsplit(':')) #It is used to split the string at the specified separator and return a list.
print(str.rstrip()) #It is used to return a right trim version of the string.
print(str.split(',')) #It is used to split the string at the specified separator and return a list.
print(str.splitlines()) #It is used to split the string at line breaks and return a list.
print(str.startswith('Hello')) #It is used to return true if the string starts with the specified value.
print(str.strip()) #It is used to return a trimmed version of the string.
print(str.swapcase()) #It is used to swap cases, lower case becomes upper case and vice versa.
print(str.title()) #It is used to convert the first character of each word to upper case.
print(str.translate('dasd'))  #It is used to return a translated string.
print(str.upper()) #t is used to convert a string into upper case.
print(str.zfill(5)) #It is used to fill the string with a specified number of 0 values at the beginning.


import sys
sys.exit(0)
print(string.ascii_letters) #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)
print(string.printable)
print(string.whitespace)

