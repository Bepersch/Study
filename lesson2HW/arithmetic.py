try:
    n = int(input("Count: "))
except ValueError:
    print("NotLikeThis")
else:
    arr = []
    s = 0
    j = n
    while n > 0:
        try:
            num = int(input("Number: "))
        except ValueError:
            print("NotLikeThis")
        else:
            if num > 0:
                s += num
            n -= 1
    print("s: ", s / j)

