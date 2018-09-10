try:
    a = int(input("Number: "))
except ValueError:
    print("NotLikeThis")
else:
    s = 0
    c = 1
    for i in str(a):
        if i != "-":
            s += int(i)
            c *= int(i)
        else:
            break
    print("s =", s, "| c =", c)
