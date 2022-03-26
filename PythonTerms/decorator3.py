import time

def time_it(funref):
    def inner_fun(val1,val2):
        start_time = time.time()
        print("Inside inner function",start_time)
        funref(val1,val2)
        end_time = time.time()
        print("Inner function completed...", end_time-start_time)
    return inner_fun

@time_it
def function_one(x,y):
    print(x,y,'function one started....')
    for item in range(10):
        time.sleep(1)
        print(item,end='\t')
    print('function one completed....')

@time_it
def function_two(x,y):
    print(x,y,'function two started....')
    for item in range(10):
        time.sleep(1)
        print(item,end='\t')
    print('function two completed....')

@time_it
def function_three(x,y):
    print(x,y,'function three started....')
    for item in range(10):
        time.sleep(1)
        print(item,end='\t')
    print('function three completed....')


function_one(1,2)
function_two(3,4)
function_three(5,6)
