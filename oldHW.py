# coding: utf-8
# %load hw1.py
def foo(*args, _type=None): 
    n1 = []
    n2 = {}
    for a in args:
        if (type(a) == _type) or (_type is None):
            if type(a) is dict:
                n2.update(a)
            else:
                if type(a) is int:
                    n1.append(a)
                else:
                    n1 += list(a)
    n3 = [n1, n2]
    print(n3)
    
