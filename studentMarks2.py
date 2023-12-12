lst=[]
for i in range(6):
    a=int(input("entetr the maeks for subjects"+str(i+1)))
    lst.append(a)
sum=0
for i in lst:
    if i<35:
        print("Fail")
        break
    else:
        sum+=i
avg=sum/6
if avg>90:
    print("A+ Grade")
elif avg>80:
    print("A grade")
elif avg>70:
    print("B+ Grade")
elif avg>60:
    print("B Grade")
elif avg>50:
    print("C+ Grade")
elif avg>40:
    print("C Grade")
else:
    print("F Grade")
