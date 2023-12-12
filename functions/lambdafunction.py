def myfun(n):
    return lambda a:a**n
x=myfun(2)
print(x(16))
