t=0
def product(a,b):
    return a*b
t=product(200,600)
print(t)
#----------------------------------------------   
t=0
def fun(a,b):
    global t
    t=a*b
fun(200,600)
print(t)
