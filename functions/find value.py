#use a  string a="print(256/2)"
#fing the value of a
a="print(256/2)"
def func(a):
    a="print(256/2)"
    print(a)
func(a)
#-----------------------------------------------------------
a="print(256/2)"
x=slice(5,8)
def func(a):
    print(a[x])
func(a)
#-------------------
def output(s):
    print(s)
    res=int(s[6:9])/int(s[10])
    return s
a="print(256/2)"
r=output(a)
print(r)
