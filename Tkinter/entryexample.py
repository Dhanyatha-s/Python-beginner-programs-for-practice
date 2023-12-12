from  tkinter import*
r=Tk()
r.title("button example")
''
r.geometry('300x200')
b=Label(r,text=input("enter the value")).grid(row=0)
e=Entry(r)
e.grid(row=0,column=1)
r.mainloop()
