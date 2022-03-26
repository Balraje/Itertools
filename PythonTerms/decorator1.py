import time

def time_it(funref):
    def inner_fun(val1,val2):
        print('Inside Inner function..')
        start_time = time.time()
        funref(val1,val2)
        end_time = time.time()
        print('Total time Required=', end_time - start_time)
        print('completed...')
    return inner_fun

@time_it
def function_two(x,y):
    print(x,y,'Inside function two...')
    for item in range(20):
        print(item,end='\t')
        time.sleep(1)


function_two(10,20)


import sys
sys.exit(0)

def time_it(funref):
    print('Inside time it')
    funref()
    print('Completed...')

def function_one():
    start_time= time.time()
    print('Inside function one...')
    for item in range(10):
        print(item,end='\t')
        time.sleep(1)
    end_time = time.time()
    print('Total time Required=',end_time-start_time)



x = function_one
time_it(x)



