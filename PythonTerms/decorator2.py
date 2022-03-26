def time_it(funref):
    def inner_fun(val1,val2):
        print('Inside Inner fun....')
        funref(val1,val2)
        print('completed....')
    return inner_fun

@time_it
def function_one(x,y):
    print(x,y,'Inside function one....')

function_one(10,20)