def roll_gen():
    count = 0
    while True:
        count = count + 1
        if count <=10:
            yield count
        else:
            break

x=roll_gen()
print(next(x))
print(next(x))
print(next(x))
print(next(x))


