try:
    a = int(input("Number: "))
except ValueError:
    print("NotLikeThis")
else:
    b = True
    i = 1
    for j in str(a):
        if j != str(a)[-i]:
            b = False
        i += 1
    print(b)
