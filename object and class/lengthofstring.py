b="hello"
a="hello!!there"
def length(a,b):
    x=slice(3,6)
    r=len(a)
    print("The length of a is: ",r)
    print(b[x])
    print(str(a) +':>'+str(b))
    print(str(a) +'  '+str(b))
length(a,b)
