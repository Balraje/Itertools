def account_no_gene():
    print('Account Generation Called...')
    count =0
    while True:
        count = count + 1
        yield count     #function Excecution paused

x=account_no_gene()
print(next(x))
print(next(x))
print(next(x))