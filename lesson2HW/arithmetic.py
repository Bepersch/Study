try:
    n = int(input("Count: "))
except ValueError:
    print("NotLikeThis")
else:
    arr = []
    s = 0
    j = 0
    while n > 0:
        try:
            num = int(input("Number: "))
        except ValueError:
            print("NotLikeThis")
        else:
            if num > 0:
                j += 1
                s += num
            n -= 1
    try:
        print("s: ", s / j)
    except ZeroDivisionError:
        print("Zero >0 numbers")
