def display():
    try:
        lst = [10, 20, 30]
        n = 10
        lst[5] = n / 0
        print(lst)
    except (ZeroDivisionError, IndexError) as e:
        print("Error:", e.args)
    else:
        print("Yes")
    finally:
        print("Yes")

display()

