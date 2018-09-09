try:
    a = int(input("Begin: "))
    b = int(input("End: "))
    c = int(input("Step: "))
except ValueError:
    print("NotLikeThis")
else:
    while a <= b:
        print("x: ", a, "| y: ", -1.24 * a ** 2 + a)
        a += c
