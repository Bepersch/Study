try:
    a = int(input("Number: "))
    n = str(input("Convert to b or kb: "))
except ValueError:
    print("NotLikeThis")
else:
    if n == "b":
        print(a, "kb =", a * 1024, "b")
    elif n == "kb":
        print(a, "b =", a / 1024, "kb")
    else:
        print("Error Input")
# new line 1
