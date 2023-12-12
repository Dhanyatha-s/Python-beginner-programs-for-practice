from  tkinter import*
r=Tk()
r.title("button example")
''
r.geometry('300x200')
def fun():
    E=e.get()
    print(E)
    l=Label(r,text=E).pack()
l=Label(r,text="KNOWX INNOVATION")
l.pack()
e=Entry(r)
e.pack()
btn=Button(r,text="Apply",fg="blue",command=fun).pack()
r.mainloop()
