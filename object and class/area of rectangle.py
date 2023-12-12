class rectangle:
    def __init__(self,l,b):
      self.l=l
      self.b=b
      print("The area of recatngle is:",l*b)
r=rectangle(10,2.05)


#-----------------------------------------------------------

class employee:
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age
        print("name=",name,"id=",id,"age=",age)
s=employee("VISWA",200,27)
setattr(s,'id',30)
#print(getattr(s,'id'))
print("the modified id is:",(getattr(s,'id')))
delattr(s,'name')
print(hasattr(s,'age'))
print(hasattr(s,'name'))
print(getattr(s,'age'))
#------------------------------------

print("the palindrome ")
def ispalindrome(p):
    return p==p[::-1]
p=str(input("enter the string"))
result=ispalindrome(p)
if result:
    print(p,"is palindrome")
else:
    print(p,"is not palindrome")
#------------------------------------------


    
    
