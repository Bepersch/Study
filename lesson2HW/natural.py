try:
    a = int(input("Number: "))
except ValueError:
    print("NotLikeThis")
else:
    s = 0
    c = 1
    for i in str(a):
        s += int(i)
        c *= int(i)
    print("s =", s, "| c =", c)
