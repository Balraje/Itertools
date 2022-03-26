import time

def time_it(funref):
    def inner_fun(*args):
        start_time = time.time()
        x = funref(*args)
        print('Result=',x)
        end_time = time.time()
        print("Inner function completed...", end_time-start_time)
    return inner_fun

def print_star(funref):
    def innner(*args):
        print("*"*40)
        result = funref(*args)
        return result
        print("*"*40)
    return innner

@time_it
@print_star
def addition(*args):
    sum=0
    for item in args:
        sum = sum + item
    return sum

@time_it
@print_star
def substraction(*args):
    sum=0
    for item in args:
        sum = sum + item
    return sum-100

@time_it
@print_star
def multiplication(*args):
    sum=0
    for item in args:
        sum = sum + item
    return sum *10

@time_it
@print_star
def division(*args):
    sum=0
    for item in args:
        sum = sum + item
    return sum/2


addition(10,20,30234,234,123123)
