try:
    a=10
    print(10/2)
    l=[10,20,30]
    print(l[7])
except ZeroDivisionError:
    print("Cannot divide by 0")
except IndexError:
    print("We cannot accet the values out of index of list")
finally:
    print("End of Program")