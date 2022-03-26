import sys
def multiplier_of(n):
    def multiplier(x):
        return x*n
    return multiplier

times3=multiplier_of(3)
times5=multiplier_of(5)
print(times3(9))
print(times5(6))
print(times5(times3(4)))

sys.exit(0)
def display(**kwargs):
    for key,value in kwargs.items():
        print('{} is {}'.format(key,value))

display(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)


sys.exit(0)
def sum(*args):
    s=0
    for item in args:
        s=s+item
    return s
sum=sum(10,20,30,40,50)
print('sum of all the elements=',sum)





sys.exit(0)
def star(func):
    def inner(*args,**kwargs):
        print('*'*30)
        func(*args,**kwargs)
        print('*'*30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print('%' * 30)
        func(*args, **kwargs)
        print('%' * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)

printer('Hello')


sys.exit(0)
def time_it(func):
    def inner(*args):
        x=func(*args)
        print('Result=',x)
        print("Inner function completed...")
    return inner

def print_star(func):
    def inner(*args):
        result=func(*args)
        print('*' * 40)
        return result
    return inner

@time_it
@print_star
def addition(*args):
    sum=0
    for item in args:
        sum = sum + item
    return sum

addition(10,20,30,40,50)

sys.exit(0)
def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print(msg)

    printer()

# We execute the function
# Output: Hello
print_msg("Hello")

sys.exit(0)
#a function can return another function.
def is_called():
    def is_returned():
        print("Hello")
    return is_returned


new = is_called()
new()


sys.exit(0)

def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operate(func, x):
    result = func(x)
    return result

print(operate(inc,3))
print(operate(dec,4))

sys.exit(0)


def fisrt(msg):
    print(msg)

fisrt('Hello')
second=fisrt
second('Hi')