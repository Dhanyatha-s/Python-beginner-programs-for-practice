
if n<=1:
    print("the negative number")
else:
    print(fib(n-1)+fib(n-2))
n=25
if n<=0:
    print("fibnacci sequence is:")
    for i in range(n):
        print(i)
n=0
n1=1
print("fibnacci sequence is:")
print(n, end=" ")
print(n1, end=" ")
n3=n1+n2
while n3<25:
    print(n1, end=" ")
    n=n1
    n1=n3
    n3=n
    print(n3)
