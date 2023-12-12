a=10
b=20
print("the two number swaped are")
a=a+b
b=a-b
a=a-b
print(a,b)
#-----------
def fact(x):
    print("the factoreal of x are",x)
    for i in range(1,x+1):
        if x%i==0:
            if i%2==0:
                print(i)
num=100
fact(num)
