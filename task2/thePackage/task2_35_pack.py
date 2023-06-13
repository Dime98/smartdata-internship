# 35. Create a python package that will store some random functions (you decide what to 
# write, at least 5), import them into another python file and use them.

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def devide(a,b):
    r = a/b if b != 0 else "zero"
    return r

def power(a,b):
    return a**b
